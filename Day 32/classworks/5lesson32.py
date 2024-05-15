# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python


def array_diff(a, b):
    result = []
    for x in a:
        if x not in b:
            result.append(x)
    return result
