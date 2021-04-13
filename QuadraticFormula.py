#quadratic formula

import cmath

print("This is a quadratic formula program for finding the values of x ")

value_of_A= float(input("Enter the value of a: "))
value_of_B= float(input("Enter the value of b: "))
value_of_C= float(input("Enter the value of c: "))


equation1=(value_of_B**2)-(4*value_of_A*value_of_C )

x1=(-value_of_B+cmath.sqrt(equation1)) /(2*value_of_A)
x2=(-value_of_B-cmath.sqrt(equation1)) /(2*value_of_A)

print("The x values are: \n x= {:g}, x= {:g} ".format(x1, x2))
