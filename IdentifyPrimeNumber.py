print("I can identify if a number is prime or not")

#ask input from user
number = int(input("Enter a number: "))
num_ctr = 0 #counter

#evaluating the number for factor
for d in range(2,number+1):
    if number%d == 0:
        num_ctr += 1
if num_ctr == 1: #num_ctr is expected to be 1 since in the range only the number itself is a factor 
    print("Number is prime")
else:
    print("NOT PRIME!!")
