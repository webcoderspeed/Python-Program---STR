# Write a Python program to remove duplicates from  Dictionary.

d = {1:1,2:2,3:1}

temp = []
res = {}
for key, value in d.items():
    if value not in temp: #Checking wheather value is present or not
        temp.append(value) # as value is not present in temp so we add it 
        res[key] = value # storing the non duplicate values to dictionary
print(res)