# Write a Python program to check if a given key already exists in a dictionary.

dictionary = {}
for key in range(1,11):
    if key not in dictionary: # checking wheather the key is present in dictionary or not
        dictionary[key] = None # adding key with value of None to dictionary
print(dictionary)       

