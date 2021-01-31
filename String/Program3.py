#Write a Python program to get a string from a given string where all occurrences of its first char have changed to ‘$’, except the first char itself.

#input() => Function used for Taking user input...
#s[0] => Pointing at the first positon of the string
#replace(old String, New String) => Function use for replacing the old string with new string 
#s[1:] => Iteration throughout the string starting from 1st Index 
# + => concatenating operator (Joins the two strings together)

s=input("Enter the String: ")
firstChar = s[0]
s = s.replace(firstChar, '$')
s = firstChar + s[1:]
print(s)