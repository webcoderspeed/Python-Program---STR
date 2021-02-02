#Write a Python program to get the second largest number from a list.

def largest_element(l): 
    if len(l)>0: # checking wheather the list its empty or not if empty it will return None
        l.sort() #sorting the list in ascending order so that we get the largest element at last of list
        return l[-2] # returning the Second last element

data = [15,2,46,25,48,35,15,75,34,29,82,100]
print(largest_element(data))




