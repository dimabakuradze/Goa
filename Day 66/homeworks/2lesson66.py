# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python



def alphabet_position(text):
    result = []
    for char in text:
        if char.isalpha():  
            if char.isupper():  
                result.append(str(ord(char) - ord('A') + 1))
            elif char.islower():  
                result.append(str(ord(char) - ord('a') + 1))
    return ' '.join(result)




