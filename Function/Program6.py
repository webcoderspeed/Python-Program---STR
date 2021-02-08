# Write a Python program to sort a list of tuples using Lambda.
# Original list of tuple:-
# [('English',88),('Science',90),('Maths',97),('Socialsciences',82)]

original_list_of_tuple =  [('English',88),('Science',90),('Maths',97),('Socialsciences',82)]

original_list_of_tuple.sort(key=lambda name:name) #Accending order of subject i:e; A-Z
print("Accending order of subject i:e; A-Z: ",original_list_of_tuple)
original_list_of_tuple.sort(key=lambda name:name, reverse=True) #Decdening order of subject i:e; Z-A
print("Decending order of subject i:e; Z-A: ",original_list_of_tuple)
original_list_of_tuple.sort(key=lambda marks:marks[-1]) #Accending order of marks i:e; 1-100
print("Accending order of marks in 1-100: ",original_list_of_tuple)
original_list_of_tuple.sort(key=lambda marks:marks[-1], reverse=True) #Decdening order of marks i:e; 100-1
print("Decending order of marks in 100-1: ",original_list_of_tuple)


