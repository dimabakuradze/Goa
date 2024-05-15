def num(number):
    list = []
    for i in number:
        if i % 2 == 0:
            list.append(i)
    return list

number = [1,2,3,4,5,6,7,8]
print(num(number))