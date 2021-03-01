#9.	Enter basic salary from the user. Write a program to calculate DA and HRA on the following conditions:-
# Salary	                                         DA	    HRA
# <=2000	                                        10%	    20%
# >2000 && <=5000	                                20%     30%
# >5000 && <=10000	                                30%	    40%
# >10000	                                        50%	    50%

#--------------------- Program ---------------------------#
salary = int(input("Enter your salary: "))
DA,HRA = None,None
if salary<=2000:
    DA = salary*10/100
    HRA = salary*20/100
elif salary>2000 and salary <=5000:
    DA = salary*20/100
    HRA = salary*30/100
elif salary>5000 and salary<=10000:
    DA = salary*30
    HRA = salary*40
elif salary>10000:
    DA = salary*50/100
    HRA = salary*50/50

print(f"Your DA: {DA} \nand HRA: {HRA} ")
