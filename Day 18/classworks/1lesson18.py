

def num(number):
    result = []
    for i in number:
        if i % 4 == 0:
            result.append(i)
    return result

number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(num(number))

