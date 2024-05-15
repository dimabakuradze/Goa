# https://www.codewars.com/kata/587731fda577b3d1b0001196/train/python


def camel_case(s):
    words = s.split()
    camel_case_words = []
   
    for word in words:
        camel_case_words.append(word.capitalize())
    camel_case = ''.join(camel_case_words)
    
    return camel_case

