""" Optional Questions for Lab 07 """

from lab07 import *

# Q6
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    # def sub(link,value):
        # if link == Link.empty:
        #     return Link.empty
        # if link.rest == Link.empty:
        #     return Link(link.first)
        # if link.rest.first == value:
        #     return Link(link.first,sub(link.rest.rest,value))
        # return Link(link.first,sub(link.rest,value))
    if link == Link.empty:
        return
    if link.rest == Link.empty:
        return
    if link.rest.first == value:
        link.rest = link.rest.rest
        remove_all(link,value)
    else: remove_all(link.rest,value)

# Q7
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    if link == Link.empty:
        return
    if isinstance(link.first,int):
        link.first = fn(link.first)
    else:
        deep_map_mut(fn,link.first)
    deep_map_mut(fn,link.rest)
    

# Q8
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    seen = []
    def iterate(link):
        if link == Link.empty:
            return False
        if link not in seen:
            seen.append(link)
            return iterate(link.rest)
        else:
            return True
    return iterate(link)

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    # double pointer
    slow, fast = link, link.rest
    while fast != Link.empty and fast.rest != Link.empty:
        if fast == slow: #or fast.rest == slow:
            return True
        else:
            fast = fast.rest.rest
            slow = slow.rest
    return False
# Q9
def reverse_other(t):
    """Mutates the tree such that nodes on every other (even_indexed) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    def reverse(t,level):
        if level % 2 == 1:
            temp = []
            for b in t.branches:
                temp.append(b.label)
            for b,label in zip(t.branches,temp[::-1]):
                b.label = label
        if t.branches:
            for b in t.branches:
                reverse(b,level+1)
    reverse(t,1)
