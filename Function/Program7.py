# 7.	Write a Python program to filter a list of integers using Lambda
# Original list of numbers:-
# [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
# Result:-
# Even number list:-
# [2 , 4 , 6 , 8 , 10]
# Odd number List:-
# [1 , 3 , 5 , 7 , 9]

original_list_of_number = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
even = lambda even: even%2==0
print("After filtering the List consisiting of Even: ",list(filter(even,original_list_of_number)))
odd = lambda even: even%2!=0
print("After filtering the List consisiting of Odd: ",list(filter(odd,original_list_of_number)))

