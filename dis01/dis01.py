def keep_ints0(cond, n):
    # python -m doctest -v dis01.py
    """
    Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints0(is_even, 5)
    2
    4
    """
    for i in range(1,n+1):
        if cond(i):
            print(i)
    
    return None

def keep_ints(n):
    """
    Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(5)(is_even)
    2
    4
    """
    def cond(func):
        for i in range(1,n+1):
            if func(i):
                print(i)
    return cond


