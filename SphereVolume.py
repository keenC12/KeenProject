import math as Math

radius = int(input("Enter radius:"))

if radius<0:
    print("Error")
else:    
    area=4*Math.pi*(radius**2)
    V=(4/3)*Math.pi*pow(radius,3)

    print("The surface are is: %.2f" %area)
    print("Volume is: %.2f" %V)
