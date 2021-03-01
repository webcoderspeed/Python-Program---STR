# 1. Write a python program that take employee id as input and display all the related department information for that employee.
# Ex: use both emp.txt and dept.txt.
# Retrieve the department_id of employee from emp.txt and then use that department_id to get information from dept.txt    

emp = open('./emp.txt','r')
dept = open('./dept.txt','r')

def main(emp, dept):
    eid = input('Enter EID: ')
    emp_record = []
    dept_record = []
    for record in emp.readlines():
        lst = record.split(',')
        if lst[0]==eid:
            emp_record.append(lst)
    for record in dept.readlines():
        lst = record.split(',')
        dept_record.append(lst)
    table = """
|----------------------------------------------------------------|
| Department_Id | Department_Name  |  Manager_Id  |  Location_Id |
|----------------------------------------------------------------|
"""
    data = ''
    for employee_record in emp_record:
        for department_record in dept_record:
            if employee_record[-1].rstrip('\n')==department_record[0]:  # finding a match for department ID in emp.txt and dept.txt file
                data = f'\n|     {department_record[0]}        |     {department_record[1]}     |      {department_record[2]}     |      {department_record[3]}'
                table+=data 
    if len(data)>3: # just to make sure that we have some data to put inside the table 
        print(table)
    else:
        print('No Record Found!')
    emp.close()
    dept.close()

main(emp, dept)


