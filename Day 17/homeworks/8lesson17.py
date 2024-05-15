def num(number):
    list = []
    for i in number:
        if i > 10:
            list.append(i)
    return list

number = [1,2,3,4,5,6,7,8,9,10,11,12]
print(num(number))