#Write a program to remove all the duplicate elements from list.

def remove_duplicate_element(l):
    res = []
    [res.append(i) for i in l if i not in res] 
    return res

data1 = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test','Hello']
data2 = [5,1,25,1,342,55,26,34,15,1,25,26]
print(remove_duplicate_element(data1))
print(remove_duplicate_element(data2))

# Alternate Way
print(set(data1)) #covert the list into set