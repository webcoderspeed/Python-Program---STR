# Write a Python program to generate nth Fibonacci term using function.

#logic
'''
# first write the logic of fibonacci series. 
    then it can be calculated as
                                                                                            5
                                                                       4                                         3
                                                        3                          2                  2                   1
                                                2             1            1            0     0            1       0         1

from the above diagram it is seen that the fibonacci can be calculated with help of previous fibonacci as in above example if want to find the calculate the fibonacci of 5 we need the fibo(5) = fibo(4) + fibo(3)
similarly for nth term we can calculate it by using fibo(n) = fibo(n-1) + fibo(n-2)
so if we want to calculate the fibonacci upto 40-50 number it can be calculated but its reduces the performance of system because we are directly calculating them and not using the using the previous fibonacci value because we are not storing them.

Now lets start by creating a dictionary and start storing the value of new fibonacci if its not present in dictionary in that way we can make our program more memory efficient as we can directly calculate the fibonacci of the number by using previous fibonacci with the of help of key value
'''

start = int(input("Enter the Number: "))

def mydic(fibo):
    d = {}
    def fibologic(number):
        if number not in d:
            d[number] = fibo(number)
        return d[number]
    return fibologic
        
@mydic        
def fibo(number):
    if number<=1:
        return number
    return fibo(number-1)+fibo(number-2)

for number in range(start+1):
    print(number,":",fibo(number))


































