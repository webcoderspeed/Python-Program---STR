# Write a Python program to remove a key from a dictionary.
# d = {'a':1,'b':2,'c':3,'d':4}

d = {'a':1,'b':2,'c':3,'d':4}
key = input("Enter the Key you want to remove: ")
if key in d:
    value = d.pop(key) # pop is function which take key in string format and remove it and return its value
    print(f"Dictionary d after removing the key {key} : {d}\nand the value of removed key : {value}")
else:
    print("Entered key is not present in dictionary")