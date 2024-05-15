def num(number):
    list = []
    for i in number:
        if i[0] == "a":
            list.append(i)
    return list

number = ["dima","babaiga",'anastasia']
print(num(number))