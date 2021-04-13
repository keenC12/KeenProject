#First n Fibonacci series
nTerms = int(input("Enter number of terms: "))

#Testing
#nTerms = 7

#Control terms
n1, n2 = 0,1
nthTerm = 0
fibonacciSqnc = []
n_ctr = 0

#Evaluation of nTerms input
if nTerms <= 0:
    print("Error!! Please input positive number")

elif nTerms == 1:
    fibonacciSqnc.append(n1)
    
else:
    while n_ctr < nTerms:
        fibonacciSqnc.append(n1) #adds the generated term to fibonacciSqnc list
        nextN= n1 + n2
        n1=n2
        n2= nextN
        
        n_ctr += 1    
        
#Prints the terms in the list
print("The first {} terms in the Fibonacci sequence:".format(nTerms))
for n in fibonacciSqnc:
    print(n)
    
    
