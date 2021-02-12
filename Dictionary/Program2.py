# 2. Write a Python program to concatenate following dictionaries 
#    to create a new one.
#    d1={1:100, 2:200}
#    d2={3:300, 4:400}
#    d3={5:500, 6:600}

d1={1:100, 2:200}
d2={3:300, 4:400}
d3={5:500, 6:600}

newDictionary = {}
for d in (d1,d2,d3):
    newDictionary.update(d) # passing the iterator to update function of dictionary
print(newDictionary)


