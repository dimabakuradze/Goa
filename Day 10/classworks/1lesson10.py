Age = int(input("შემოიტანე შენი ასაკი: "))

if Age <= 0 or Age > 100:
    print("არის მოხუცი")

elif Age <= 12:
    print("ბავშვი")

elif Age <= 18:
    print("თინეიჯერი")

elif Age <= 60:
    print("სრულწლოვანი")

else:
    print("მოხუცი")