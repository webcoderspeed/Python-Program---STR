# Write a Python program to sum all the items in a dictionary.

dictionary = {i:i*i for i in range(1,11)}
print(dictionary)
print("Sum of all items of dictionary: ",sum(dictionary.values()))