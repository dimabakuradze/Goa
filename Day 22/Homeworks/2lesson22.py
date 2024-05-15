# codewars 7-kyu


# 1 -Square Every Digit


# def square_digits(num):
#     res_str = ""
#     num_str = str(num)
#     for i in num_str:
#         res_str += str(int(i)**2)
#     return int(res_str)


# print(square_digits(9199))


# 2 - Vowel Count


# def get_count(sentence):
#     count = 0
#     vowels = ["a","e","i","o","u"]
#     for char in sentence:
#         if char in vowels:
#             count+=1
#     return count


# 3 - More than Zero?

# def corrections(x):
#     if x > 0:
#         return f"{x} is more than zero"
#     else:
#         return f"{x} is equal to or less than zero"


# 4 - leap years

# def is_leap_year(year):
#     leap = False
    
#     if year % 400 == 0:
#         leap = True
#     elif year % 4 == 0 and year % 100 != 0:
#         leap = True
    
#     return leap


# 5 - shortes word 


# def find_short(s):
#     return min([len(word) for word in s.split()])