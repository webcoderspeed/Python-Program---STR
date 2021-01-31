#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

#input() => Function used for Taking user input...
# s[0:2] => Iterating through the string upto 2 character staring from 0 Index 
# s[2:] => Again iterating through the string and staring from 2(second last position) to last position
# + => concatenating operator (Joins the two strings together)

s1 = input("Enter the String1: ")
s2 = input("Enter the String2: ")

st1 = s1[0:2] + s2[2:]
st2 = s2[0:2] + s1[2:]
print(st2,st1)