#Write a Python program to remove the characters which have odd index values of a given string.

#input() => Function used for Taking user input...
# s[0::2] => Iterating through the string starting from 0 Index and increase the value of index value by 2
# s[staringIndex,endingIndex,steps] => In this case step value is 2 therefore it neglect the odd value by default its 1 if not mentioned any 

s = input("Enter the String: ")
removeOddString = s[0::2]
print(removeOddString)