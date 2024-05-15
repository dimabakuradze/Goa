num = int(input("sheiyvane mteli ricxvi:"))
num1 = int(input("sheiyvane mteli ricxvi:"))

list = []
for i in range(num,num1 + 1):
    list.append(i)
for num in list:
    if num % 5 == 0:
        print(num)


