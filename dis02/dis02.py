def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if m == 1:
        return n
    return multiply(m-1,n) + n

def countdown(n):
    """
    >>> countdown(3)
    3
    2
    1
    """
    print(n)
    if n>=2:
        countdown(n-1)

def sum_digits(n):
    """
    >>> sum_digits(7)
    7
    >>> sum_digits(30)
    3
    >>> sum_digits(228)
    12
    """
    if n<10:
        return n
    return sum_digits(n//10) + n%10

def inverse_cascade(n):
    grow(n)
    print(n)
    #shrink(n)

def grow(n):
    if n:
        grow(n//10)
        print(n)


def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    total = 0
    if n==0:
        return 1
    if n<0:
        return 0
    for i in range(1,k+1):
        total += count_k(n-i,k)
    return total