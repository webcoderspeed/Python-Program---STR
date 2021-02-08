# Write a python program to print all alphabets from a to z. - using while loop

res = "" 
index = 97 # Integer value of a = 97
while index!=123: # Integer value of z = 123
        res+=chr(index) # chr() take iterable as input and convert them into ASCII character
        index = index+1
print(res)

