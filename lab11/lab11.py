""" Lab 11: Iterators and Generators """

# Q1
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    # using a loop
    # for i in s:
    #     yield i*k

    # using yield from
    yield from map(lambda x: x*k,s) # 套了map也是iterator!整挺好

# Q2
def trap(s, k):
    """Return a generator that yields the first K values in iterable S,
    but raises a ValueError exception if any more values are requested.

    >>> t = trap([3, 2, 1], 2)
    >>> next(t)
    3
    >>> next(t)
    2
    >>> next(t)
    ValueError
    >>> list(trap(range(5), 5))
    ValueError
    >>> t2 = trap(map(abs, reversed(range(-6, -4))), 2)
    >>> next(t2)
    5
    >>> next(t2)
    6
    >>> next(t2)
    ValueError
    """

    count = 0
    for i in s:
        yield i
        count += 1
        if count >= k:
            raise ValueError



# the naturals generator is used for testing scale and merge functions
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1