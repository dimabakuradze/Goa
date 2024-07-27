Email = input("Enter your email: ")
password = input("Enter your password: ")
Age = int(input("Enter your age: "))
email_password = ("you succesfuly joined your account")

if Email == "xatunan12@gmail.com":
 print("this email is correct")

else:
  print("your email is not correct")

if password == "daduka123":
  print("password is correct")
  print(email_password)

else:
  print("your password is not correct")

if Age >= 50:
  print("you are old")

elif  Age >= 18:
  print("your an a adult")

else:
  print("your not an adult")