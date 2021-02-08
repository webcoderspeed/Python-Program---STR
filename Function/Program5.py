# Write a python program to find twin prime numbers up to a range.
# [ex 3,5   5,7  7,9 11,13  17,19   41,43 ] all are twin prime their number difference is 1

# logic
'''
# 2 is an even number as well as prime number therefore start the range from 2
# if number is divisible by 2 its not an prime number
# if number is divisble by divisble by 3,5,7.. its might be a prime number
# therefore number should be divisible by number itself
# for restricting the duplicacy of number we have check wheather the prime is present in list or not. 
if present then do nothing if not then add it to the list
then start by declaring a tuple and passing the resultant list as an argument in tuple for the conversion of list into tuple
'''

start = int(input("Enter the Inital Value: "))
end = int(input("Enter the Final Value: "))

def twin_prime_number(start,end):
    res = []
    for num in range(start,end+1):
        for divisor in range(2,num):
            if num%divisor == 0:
               break
        else:
            if num not in res: 
                res.append(num)   
    tup = tuple(res)
    twin=[]
    for start in range(start,len(tup)-1): # upto the range to tuple
        twin.append(tup[start:start+2]) # adding to two value of tuple at one location
    print(twin)   

twin_prime_number(start,end)