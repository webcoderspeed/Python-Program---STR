# Write a Python script to print a dictionary where the keys are 
#  numbers between 1 and 15 (both included) and the values are square of keys.

print({i:i*i for i in range(1,16)}) # using dictionary comprehension 