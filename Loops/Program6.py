# Write a python program to find sum of all natural numbers between 1 to n.

n = int(input("Enter the nth natural number"))
sum = 0
for num in range(1,n+1):
    sum += num
print("Sum of nth natural number:",sum)