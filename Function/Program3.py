# Write a Python program to print all perfect numbers between given range using functions.
#  [ perfect number is a positive integer that is equal to the sum of its positive divisor, excluding the number itself example 6   (3+2+1= 6)]

start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))
def perfect_number(start,end):
    for perfectnumber in range(start,end+1):
        sum = 0
        for divisor in range(1,perfectnumber):
            if perfectnumber%divisor == 0:
                sum += divisor
                if sum == perfectnumber:
                    print(sum)
perfect_number(start,end)

