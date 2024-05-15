num = int(input("Enter your number:"))

list = []

for i in range(num):
    if i % 2 == 0:
        list.append(i)
print(list)
    