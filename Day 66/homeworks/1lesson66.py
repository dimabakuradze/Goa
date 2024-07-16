# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python


def is_valid(braces):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in braces:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            return False
    
    return len(stack) == 0
