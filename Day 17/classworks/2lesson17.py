def num(number):
    list = []
    for i in number:
        if len(i) > 5:
            list.append(i)
    return list

number = ['dima','erekle','aramishka']
print(num(number))