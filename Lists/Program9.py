############## logic ####################

# arr = []
# print("Input:",x,y,z,n,sep='\n')
# for i in range(0,x+1):
#     for j in range(0,y+1):
#         for k in range(0,z+1):
#             if sum([i,j,k])!=n:
#                 arr.append([i,j,k])
# print(arr)



import itertools

x,y,z,n = int(input('Enter Value of x:')),int(input('Enter Value of y:')),int(input('Enter Value of z:')),int(input('Enter Value of n:'))


print([[i,j,k] for i,j,k in  itertools.product(range(x+1), range(y+1), range(z+1))if n!=([x+y+z])])



