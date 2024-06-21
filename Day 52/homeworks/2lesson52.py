# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

def descending_order(num):
    num = str(num)
    num = list(num)
    num = sorted(num)
    num = reversed(num)
    num = "".join(num)
    return int(num)