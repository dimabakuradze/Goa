def num(number):
    list = []
    for i in number:
        list.append(i)
    return list

number = input("Enter your name:")
print(num(number[::-1]))
    