# Write a python program to print multiplication table of any number.

number = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{number} X {i} =",number*i)