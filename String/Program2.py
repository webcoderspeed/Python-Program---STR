#2. Write a Python program to get a string made of the first 2 and last 2 chars from a given a string.

#input() => Function used for Taking user input...
# s[0:2] => Iterating through the string upto 2 character staring from 0 Index 
# s[-2:] => Again iterating through the string and staring from -2(second last position) to last position
# + => concatenating operator (Joins the two strings together)

s = input("Enter the String: ")
print(s[0:2]+s[-2:])
