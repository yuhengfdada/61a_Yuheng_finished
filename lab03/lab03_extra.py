""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def cycler(n):
        cycles = n // 3
        remainder = n % 3 
        def actual(num):
            for _ in range(cycles):
                num = f3(f2(f1(num)))
            if remainder == 1:
                num = f1(num)
            if remainder == 2:
                num = f1(num)
                num = f2(num)
            return num
        return actual
    return cycler


## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y*10+x%10
    while x > 0:
        x, y = x//10, f()
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)

def current_pos(n,it):
    if it==1:
        return True
    if n%it==0:
        return False
    else:
        return current_pos(n,it-1)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    return current_pos(n,n-1)
    

def odd(n,odd_term,even_term):
    return even(n-1,odd_term,even_term) + odd_term(n)

def even(n,odd_term,even_term):
    if n==0:
        return 0
    return odd(n-1,odd_term,even_term) + even_term(n)

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    if n%2:
        return odd(n,odd_term,even_term)
    return even(n,odd_term,even_term)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def count_digit(digit, number):
        if number < 10 and number == digit:
            return 1
        elif number < 10 and number != digit:
            return 0
        elif number % 10 == digit:
            return 1 + count_digit(digit, number // 10)
        else:
            return count_digit(digit, number // 10)

    def helper(n):
        if n < 10:
            return 0
        else:
            return count_digit(10 - n % 10, n // 10) + helper(n // 10)

    return helper(n)

