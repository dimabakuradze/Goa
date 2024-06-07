# https://www.codewars.com/kata/514a6336889283a3d2000001/train/python


def get_even_numbers(arr):
    result = []
    
    for i in arr:
        if i % 2 == 0:
            result.append(i)
    return result