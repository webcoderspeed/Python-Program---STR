# Write a program to determine frequency of number in a list of numbers.

dictionary = {}
data = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test','Hello',5,1,25,1,342,55,26,34,15,1,25,26]
for value1 in data:
    frequency = 0 # Once the value is checked we again the set frequency to Zero
    for value2 in data:
        if value1 == value2: # Matching value 1 with value 2
            frequency = frequency+1 # Increasing the frequency value by 1
            dictionary[value1] = frequency #Over-riding the previous value key value with new one
print(dictionary)
    