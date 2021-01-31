#Write a Python program to remove the nth index character from a nonempty string.

##input() => Function used for Taking user input...
#int() => function use to convert string into Interger
#range() => function use to define the range of for loop(iterator)
#continue => keyword use to send the index value again to iterator to increase it according to given condition
# and in simple word continue keyword is used pass the control to iterator

s = input("Enter the String: ")
nChar = int(input("Enter a nth Character Position: "))
for index in range(0,len(s)):
    if(index == nChar):
        continue
    else:
        print(s[index],end='')
