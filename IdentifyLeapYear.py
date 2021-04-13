year = int(input("Enter a year: ")) #Ask user input for Year

#Checking the year if it is leapyear
if year%4 == 0:
    if year%400 == 0:
        print("It is a leapyear")
    else:
        print("It is not a leapyear")
else:
    print("It is not a leapyear")
