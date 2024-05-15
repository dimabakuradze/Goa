name = int(input('enter your first number: '))  # 1-li
print(name > 1 and name < 5 ) 


number = int(input("Enter your second number: "))       # 2-re
number = (number % 5 == 0 and number % 10 == 0)
print(number)


number1 = int(input("Enter your third number: "))         # 3-me
number1 = (number1 <= 5 and number1 <= 15)         
print(number1)

number2 = int(input("Enter your forth number: "))       # 4-e
number2 = (number2 != 15 and number2 != 10)
print(number2)

number3 = int(input("Enter your fifth number: "))      # 5-e
number3 = (number3 < 5 and number3 <10)
print(number3)

number4 = int(input("Enter your sixth number: "))       # 6-e
number4 = (number4 % 15 != 0 and number4 % 20 != 0)
print(number4)

number5 = int(input("Enter your seventh number: "))       #7-de
number5 = (number5 >= 10 and number5 >= 25)
print(number5)
 
number6 = int(input("Enter your eights number: "))        #8-e         
number6 = (number6 ** 5 and number6 ** 2)
print(number6)

number7 = int(input("Enter your ninth number: "))      #9-e
number7 =(number7 % 5 // 0 and number7 % 15// 0)
print(number7)

number8 = int(input("Enter your tenth number: "))       #10-e
number8 = int(number8 % 20 - 5 and number8 % 25 - 5)  
print(number8)