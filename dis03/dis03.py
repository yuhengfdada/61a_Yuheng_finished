# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)
# Selectors
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
# For convenience
def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


t = tree(1,
[tree(3,
[tree(4),
tree(5),
tree(6)]),
tree(2)])

def tree_max(t):
    if is_leaf(t):
        return label(t)
    return max(label(t),max([tree_max(b) for b in branches(t)]))

def tree_height(t):
    if is_leaf(t):
        return 0    # leaf node has height 0
    return 1+max([tree_height(b) for b in branches(t)])

def square_tree(t):
    return tree(label(t)**2,[square_tree(b) for b in branches(t)])

def find_path(tree,x):
    if label(tree) == x:
        return [x]
    for b in branches(tree):
        if not find_path(b,x):
            continue
        if x in find_path(b,x): # key step
            return [label(tree)]+find_path(b,x)
    return None

def prune(t,k):
    if k==0:
        return tree(label(t))
    return tree(label(t),[prune(b,k-1) for b in branches(t)])