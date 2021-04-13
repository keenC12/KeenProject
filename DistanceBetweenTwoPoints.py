import math as Math


pointX1, pointY1=(int(pointX1) for pointX1 in input("Enter first point x, y: ").split(","))

pointX2, pointY2=(int(pointX2) for pointX2 in input("Enter second point x, y: ").split(","))

toBeSquared =(pow((pointX2-pointX1),2)) + (pow((pointY2-pointY1),2))

distance=Math.sqrt(toBeSquared)

print("The distance between the two points is: %.2f" %distance)
