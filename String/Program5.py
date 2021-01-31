#Write a Python program to add ‘ing’ at the end of a given string(length should be at least 3). If the given string already ends with ‘ing’ then add ‘ly’ instead. If the string length of the given is less than, leave it unchanged.

#input() => Function used for Taking user input...
#len() => function use to count the length
# + => concatenating operator (Joins the two strings together)

s=input("Enter the String: ")
res  = None
if(len(s)>3):
    res = s[0:]+'ing'
    if(s.endswith('ing')):
        res = s[0:]+'ly'
print(res)