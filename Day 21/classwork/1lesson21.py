"""Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
"""


def multiply(values):
    result = 1
    for num in values:
        result *= num
    return result

print(multiply([1, 2, 3, 4])) 