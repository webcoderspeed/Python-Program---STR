# Write a python program to display a greet message according to the marks obtained by the student.

#--------------------- Program ---------------------------#
marks = int(input("Enter your marks: "))
if marks>90:
    print("Excellent")
elif marks>=80:
    print("Very Good")
elif marks<=70 and marks>=60:
    print("Good")
elif marks<=50 and marks>=40:
    print("Work Hard you can do much better")
else: 
    print("Sorry you failed, better luck next time")

