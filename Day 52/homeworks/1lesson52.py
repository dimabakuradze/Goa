# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def get_count(sentence):
    result = 0
    
    for i in sentence:
        if i in "aeiou":
            result+=1
    return result