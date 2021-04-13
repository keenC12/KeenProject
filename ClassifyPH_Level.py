
#Indefinite loop until a result is given
while True:
    #ask user input
    ph = float(input("Enter pH level: "))
    if ph < 0 or ph >14:#check if inputted value is within range
        print("Error, input other value")
        continue#returns to ask user for input
    elif ph <= 6:#check for acidec level
        print("pH level {} is acidic ".format(ph))
    elif ph == 7:#check for neutral level
        print("pH level {} is neutral".format(ph))
    elif ph >= 8:#check for base level
        print("pH level {} is base ".format(ph))    
    break   #stops the indefinite loop once result is given 
