# Write a Python program to print all Armstrong numbers between given range using functions.

# Example of Armstrong Number:
    # number = 153
    # armstrong = pow(1,3)+pow(5,3)+pow(3,3) =  153

#logic:
'''
# first assign the number to temporary variable for future checking
# find the order of the number (example: 153 => order is 3 because its length is 3)
# define a varible having initial value of zero (example: armstrong = 0)
# find the digit by using % operator 
# then add the armstrong number to pow(digit,order)
# then remove the last digit of the temporary variable by using // operator 
# if number == armstrong then print it
'''

start = int(input("Enter the Inital Value: "))
end = int(input("Enter the Final Value: "))

def armstrong(start,end):
    for num in range(start,end):
        temp = num
        order = len(str(num))
        armStrong = 0
        while temp>0:
            digit = temp%10
            armStrong += pow(digit,order)
            temp //= 10
        if num==armStrong:
            print(armStrong)

armstrong(start,end)

