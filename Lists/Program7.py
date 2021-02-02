#Write a Python program to count the number of strings where the string length is 4 or more and then first and last character are same from a given list of strings.

def first_character_and_last_character(l):
    return [i for i in l if len(i)>3 and i[0].upper() == i[-1].upper()]

data1 = ['wow', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test','Hello','maam','saas']

print(first_character_and_last_character(data1))
