# Topic: itertools and functools
# itertools: chain, islice, groupby, product, combinations, permutations
# functools: partial, lru_cache, reduce

import itertools
import functools

# --- itertools ---
# TODO: Use chain to combine two lists into one iterable
a = [1, 2, 3]
b = [4, 5, 6]

# TODO: Use islice to get first 5 elements from a generator
def infinite_counter(start=0):
    while True:
        yield start
        start += 1

# TODO: Use groupby to group sorted words by first letter
words = ["apple", "avocado", "banana", "blueberry", "cherry"]

# TODO: Use product to get all (row, col) pairs in a 3x3 grid

# TODO: Use combinations and permutations on ['A', 'B', 'C']

# --- functools ---
# TODO: Use partial to create a base-2 log function from math.log
import math

# TODO: Use lru_cache to memoize a fibonacci function
@functools.lru_cache(maxsize=None)
def fib(n):
    pass

# TODO: Use reduce to compute the product of a list
numbers = [1, 2, 3, 4, 5]
