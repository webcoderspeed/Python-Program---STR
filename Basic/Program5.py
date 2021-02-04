# Write a Python program to perform swapping of two numbers with or without third variable.

#--------------------- Program ---------------------------#
num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the Second Number: "))
num1,num2 = num2,num1
print(f"Numbers after Swapping \n\t num1: {num1} and num2:{num2}")