# Write a python program to find sum of first and last digit of a number.

number = int(input("Enter the number: "))
digit = str(number) # converting the entered number into string because string is iterable and therefore we can find any value by using the index value of the number 
sum = int(digit[0]) + int(digit[-1]) # converting the digit again into integer so that we can perform arthmatic operation in this case add operation 
print("Sum of first and last digit of entered number: ",sum)