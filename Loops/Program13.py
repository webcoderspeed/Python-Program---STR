# Write a python program to calculate sum of digits of a number.

number = int(input("Enter the number: "))
num = str(number)# converting the entered number into string because string is iterable and therefore we can find any value by using the index value of the number 
sum = 0
for i in num:
    sum += int(i) # fetching each value of specific index and converting them into integer and then performing add operation
print("Sum of entered digit: ", sum)


