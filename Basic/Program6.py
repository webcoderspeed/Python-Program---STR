# Write a Python program that read a 3 digit number from user and perform the addition of their digits.

#--------------------- Program ---------------------------#
threeDigitNumber = input("Enter the Three Digit Number: ")
res = 0
for i in threeDigitNumber:
    res += int(i)
print("Sum of Three Digit Number: ",res)
