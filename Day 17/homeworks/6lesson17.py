def num(number):
    list = []
    for i in number:
        list.append(i * i)
    return list

number = [1,2,3,4,5]
print(num(number))