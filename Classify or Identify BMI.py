#This is a program to identify BMI

firstName=input("Enter first name: ")
lastName=input("Enter last name: ")

weightInPounds=float(input("Enter your weight in pounds: "))
heightInInchies=float(input("Enter height in inches: "))

BMI=(weightInPounds*720)/(heightInInchies**2)



if BMI>=19:
    if BMI<=25:
        print(firstName, lastName, "\nYour BMI is",end= ":")
        print("%.0f"%BMI)
        print("Your BMI is within the healthy range")
    else:
        print(firstName, lastName, "\nYour BMI is",end= ":")
        print("%.0f"%BMI)
        print("Your BMI is over the healthy range")
elif BMI<19:
    print(firstName, lastName, "\nYour BMI is",end= ":")
    print("%.0f"%BMI)
    print("Your BMI is below the healthy range")
