# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python


def first_non_repeating_letter(s):
    sss = s.lower()  
    
    for i in range(len(s)):
        if sss.count(sss[i]) == 1:  
            return s[i] 
    return "" 