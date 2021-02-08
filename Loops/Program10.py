# Write a python program to count number of digits in a number.

print("Number of digit in entered number",len(input("Enter the Number:"))) # problem user can enter any type of value such as string, list, etc.

# '''
# Best way:
number = int(input("Enter the number: ")) # restricting the user to enter the number only
count = len(str(number))
print("Number of digit in entered number:", count)
# '''