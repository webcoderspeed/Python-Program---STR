# 1.	Write a python menu driven program which help to manage departments of the company.The program must have the following functionalities
# a.	View all departments
# b.	Search departments by  
# i.	department_id
# ii.	department_name 
# c.	Insert a new department
# d.	Update information of an existing department
# e.	Delete a department by department id.
# All the task should be performed on depart.txt file  that is uploaded with the assignment

import os
import re

dept = open('./dept.txt','r')

def view_all_department():
    for rec in dept.readlines():
        print(rec,end='')

def search_department():
    def search_by_department_id():
        department_id = input('Enter Department ID: ')
        for rec in dept.readlines():
            lst = rec.split(',')
            if lst[0]==department_id:
                print(f'Record Found: {rec}')
                break
        else:
            print("No record Found!")
        
    def search_by_department_name():
        dname = input('Enter Department name: ')
        for rec in dept.readlines():
            lst = rec.split(',')
            if lst[1].lower() == dname.lower():
                print(f'Record Found: {rec}')
                break
        else:
            print("No record Found!")
    while True:
        os.system('cls')
        choice = int(input("""-------------------  MAIN MENU   ----------------------
            1) Search Department by ID 
            2) Search Departments by Name
            3) Exit 
            Enter your choice: """))
        if choice == 1:
            search_by_department_id()
        elif choice==2:
            search_by_department_name()
        elif choice==3:
            break
        else:
            print('Invalid Choice...')
        os.system('pause')

def insert_record():
    department_id = input('Enter Department ID: ')
    department_name = input('Enter Department Name: ')
    manager_id = input('Enter Manager ID: ')
    location_id = input('Enter Location ID: ')
    dept = open('./dept.txt','a')
    record = f'\n{department_id},{department_name},{manager_id},{location_id}'
    dept.write(record)
    dept.close()

def update_record():
    def update_department_name():
        old_department = input('Enter Department Name: ')
        department_name = input('Enter New Department Name: ')
        with open('./dept.txt', 'r+') as dept:
            text = dept.read()
            text = re.sub(old_department, department_name, text)
            dept.seek(0)
            dept.write(text)
    def update_department_manger_id():
        old_department = input('Enter Manager ID: ')
        department_name = input('Enter New Manager ID: ')
        with open('./dept.txt', 'r+') as dept:
            text = dept.read()
            text = re.sub(old_department, department_name, text)
            dept.seek(0)
            dept.write(text)
    while True:
        os.system('cls')
        choice = int(input("""-------------------  MAIN MENU   ----------------------
            1) Update Department Name
            2) Update Manager ID
            3) Exit 
            Enter your choice: """))
        if choice == 1:
            update_department_name()
        elif choice==2:
            update_department_manger_id()
        elif choice==3:
            break
        else:
            print('Invalid Choice...')
        os.system('pause')
    
def delete_record():
    department_id = input('Enter Department ID: ')
    dept = open('./dept.txt','r')
    res = []
    for rec in dept.readlines():
        lst = rec.split(',')
        if lst[0]!=department_id:
            res.append(lst)
    dept.close()
    dept = open('./dept.txt','w')
    for record in res:
        record = f'{record[0]},{record[1]},{record[2]},{record[3]}'
        dept.write(record)
    dept.close()
    

def main():
    while True:
         os.system('cls')
         choice = int(input("""-------------------  MAIN MENU   ----------------------
            1) View All Departments 
            2) Search Departments
            3) Insert A New Department
            4) Update information of an existing department
            5) Delete a department by department ID
            6) SignOut
            Enter your choice: """))
         if choice == 1:
             view_all_department()   
         elif choice == 2:
             search_department()
         elif choice == 3: 
             insert_record()
         elif choice == 4:
             update_record()
         elif choice == 5:
             delete_record()
         elif choice == 6:
             print('You are Successfully logged out! :)')
             break
         else:
             print('Invalid Choice...')
             dept.close()
         os.system('pause')
main()


