age = int(input("შემოიტანე შენი ასაკი: "))

if age <= 0 or age > 100:
    print("არის მოხუცი")

elif age <= 12:
    print("ბავშვი")

elif age <= 18:
    print("თინეიჯერი")

elif age <= 60:
    print("სრულწლოვანი")

else:
    print("მოხუცი")