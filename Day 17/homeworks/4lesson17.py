def num(number):
    list = 0
    for i in number:
        if list < i:
            list = i
    return list

number = [1,2,3,4,5,6]
print(num(number))
    
    