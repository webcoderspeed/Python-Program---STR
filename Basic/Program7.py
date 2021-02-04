# Write a python program to find the greatest number among three.

#--------------------- Program ---------------------------#
num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the Second Number: "))
num3 = int(input("Enter the Third Number: "))

if num1>num2 and num1>num3:
    print("First number is the greatest among three entered number: ",num1)
elif num2>num1 and num2>num3:
    print("Second number is the greatest among three entered number: : ",num2)
else:
    print("Third number is the greatest among three entered number: ",num3)

# Atlernate way
print("Greatest Element:",max(num1,num2,num3))