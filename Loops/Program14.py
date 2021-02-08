# Write a python program to calculate product of digits of a number.

number = int(input("Enter the number: "))
num = str(number)# converting the entered number into string because string is iterable and therefore we can find any value by using the index value of the number 
multiply = 1 # intialising it by one(1) because if we initialise with Zero(0) then the resultant will be zero
for i in num:
    multiply *= int(i) # fetching each value of specific index and converting them into integer and then performing multiplication operation
print("Sum of entered digit: ", multiply)


