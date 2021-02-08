#3.	Write a Python program which accepts the radius of a circle from the user and compute the area.

#-----------------------Program-----------------------------#
import math
radius = int(input("Enter the Radius of the Circle: " ))
area = math.pi * radius*radius
print(area)