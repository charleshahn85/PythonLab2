import math

name = "Charlie Hahn"
age = 38
height = 5.9
favorite_color = "yellow"

print(name)
print(age)
print(height)
print(favorite_color)

print("My name is",name,"and I am",age,"years old.")

print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite Color {favorite_color} 
""")

circle_area=(math.pi)*(5**2)
print ("Area of circle if radius is 5 non rounded is",circle_area)
circle_area_rounded=round(circle_area)
print ("Area of circle if radius is 5 round is",circle_area_rounded)

A=math.sqrt(age)
print ("The square root of my age is",A)
B=math.sin(height)
C=math.cos(height)

print ("The sine value of my height is",B)
print ("The cos value of my height is",C)

D=age+5
E=height-4
F=age*height
G=age%3
H=age**2

print (f"""

My age plus 5 is {D}
My height minus 4 is {E}
My age times my height is {F}
My remainder of my age divided by 3 is {G}
My age to the second power is {H}
""")

tempa=input("What is the temperature outside in fahrenheit measurement?")
tempb=int(tempa)
tempc=(tempb-32)*5/9
tempd=int(tempc)

print("The celsius temperature outside is",tempd,"°C")