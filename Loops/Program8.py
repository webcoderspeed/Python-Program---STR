# Write a python program to find sum of all odd numbers between 1 to n.

nth =int(input("Enter the nth number: "))
sum = 0
for num in range(1,nth+1):
        if  num%2!=0:
            sum+=num
print(f"sum of odd number in range 1 to {nth}: ",sum)        