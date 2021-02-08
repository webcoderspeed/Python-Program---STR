# Write a python program to find first and last digit of a number.

number = int(input("Enter the number: "))
digit = str(number) # converting the entered number into string because string is iterable and therefore we can find any value by using the index value of the number 
print("First digit of Entered number: ", digit[0]) # as in this case the first character is on index 0(Zero)
print("Last digit of Entered number: ", digit[-1]) # last character is on index -1