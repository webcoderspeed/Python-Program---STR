# Write a Python program to sort a dictionary by key. 

d = {"z":2,'a':7,'7':'a',"2":'z'}
for key in sorted(d): # sorted function will sort the key of dictionary 
    print(key,":", d[key]) # here we are fetching the value in sorted order of keys
