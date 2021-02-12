#Write a Python program to multiplies all the items in a list.

def multiply_all_elements_of_list(l):
    n = int(input("Enter the number by which you want to multiply the list: "))
    return [i*n for i in l] #using list comprehension 

#list compreshension - 
# [output iteration conditon]
data = [1,2,3,4,5,6]
print(multiply_all_elements_of_list(data))