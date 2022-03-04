"""
reduce() function is applied to an iterable and reduce it to a single
            commulative value.
            performs on first two elemets and repeats the prcess until
            1 value remains.
reduce(function, iterable)
"""

# Example

import functools

letter = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y: x + y,letter)
print(word)

factorial = [5,4,3,2,1]

result = functools.reduce(lambda x, y: x * y,factorial)
print(result)