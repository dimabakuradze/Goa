# https://www.codewars.com/kata/61c78b57ee4be50035d28d42/train/python



def overlap_merge(str1, str2):
    max_overlap = 0
    overlap_length = 0
    

    for i in range(1, min(len(str1), len(str2)) + 1):
        if str1[-i:] == str2[:i]:
            overlap_length = i
    return str1 + str2[overlap_length:]

