# Write a Python program to find all prime numbers between given range using functions.


# logic
'''
# 2 is an even number as well as prime number therefore start the range from 2
# if number is divisible by 2 its not an prime number
# if number is divisble by divisble by 3,5,7.. its might be a prime number
# therefore number should be divisible by number itself 
'''

start = int(input("Enter the Inital Value: "))
end = int(input("Enter the Final Value: "))

def prime_numbers(start,end):
    if start>1:
        print([num for num in range(start,end) if all(num%divisor!=0 for divisor in range(2,num))])
    else: 
        print("Make Sure the Entered inital value is greater than 1")

prime_numbers(start,end)













