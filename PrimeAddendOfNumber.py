
def main():
    while True:
        n = int(input("Input n: "))
        if even(n) == "True":
            if prime(n) == "True":
                prime
            break
        else:
            print("Error, input different number")
            continue
def even(x):
    if x % 2 == 0:
        if x <= 2:
            x = "False"
        else:
            x = "True"
    else:
        x = "False"
    return x
def prime (y):
    primeList = []
    for i in range (3,y):
        num_ctr = 1
        for j in range (2,i):     
            if i % j == 0:
                num_ctr += 1
        
        if num_ctr == 1:
            primeList.append(i)
    
    #finding pairs
    for n in primeList:
        b = y-n
        if b in primeList:
            if n > b in primeList:
                print("The two prime numbers are {}  and {}".format(n,b)) 
                break
            
    
    

main()     
