#Determine is number is divisible by 2
#
def dvd_2 (number):
    if number%2 == 0:
        return print(number, "is divisible by two, it is even")
    else:
        return print(number, "is not divisible by two, it is odd")


def main ():
    number = int(input("Enter a number: "))
    dvd_2(number)

action = input("Do you want to enter a number? ")

if action.lower() == "yes":
    while True:

        main() 

        action = input("Do you want to enter another number? ")
         
        if action.lower() == "no":
            print("Thank you, Come again")
            break
        else:
            print("Input invalid\nTry Again.\nRerun Program")
            break

        
        
elif action.lower() == "no":
    print("Thank you, Come again")
else:
    print("Input invalid\nPlease Rerun program.")
