
# print the list of item in for loop
'''
l = [1,2,3,4,"susant" ,"kumar" , 45.56]
for i in l:
    print(i)
'''
# for loop with else blocl
'''
l = [1,2,3,4,"susant" ,"kumar" , 45.56]
for i in l:
    print(i)
else:
    print("else block")
'''
# use of pass in for loop
'''
l = [1,2,3,4,"susant" ,"kumar" , 45.56]
for i in l:
    pass
'''
# extract each letter from the name
'''
name = 'sushanta'
for i in name:
    print(i)
'''

# print only integer from the list by using break
'''
l = [1,2,3,4,"susant" ,"kumar" , 45.56]
for i in l:
    if (i=='susant'):
        break
    print(i)
else:
    print("else block")  # else block won't be execute if we use break
'''

# print till 'S' from name 'RITESH' by using of break
'''
n = 'RITESH'
for i in n:
    if i=='S':
        break
    print(i)
else:
    print("Else block")
'''

# tuple elements
'''
t = (1,2,3,4,'susant')
for i in t:
    print(i)
print(type(t))
'''

# set elements
# set() removes duplicate elements
'''
s = {2,3,2,3,2,"susanta"}
for i in s:
    print(i)
print(type(s))
'''

# dict elements
#d = {'id':101, 'name':'susant','profession':'software engineer'}

# fetch index and values - items()
'''
for k,v in d.items():
    print(k,v)'''

# fetch only values - values()
'''
for v in d.values():
    print(v)
'''

# fetch only keys
'''
for k in d.keys():
    print(k)'''

# another ay to fetch keys and values without using items()
'''
for i in d:
    print(i, ':', d[i])'''
'''
print(d['name'])
print(d['id'])
'''
'''
# range()
print(range(9)) # range(0,9)
print(list(range(9)))  #[0, 1, 2, 3, 4, 5, 6, 7, 8]
'''
'''
for i in range(9):
    print(i)'''
'''
print(list(range(0,9,2)))
# range 0-9 and jump/step size =2 # [0, 2, 4, 6, 8]

print(list(range(0,9,-1)))
# [] , empty list due to step is negative but range in positive direction

print(list(range(9,0,-1)))
# [9, 8, 7, 6, 5, 4, 3, 2, 1] , direction is 9 to 0 , and step is -1
'''

# nested for loop
'''
for i in range(5):
    for j in range(0,i+1):
        print("susant", end= " ")
    print('\n')'''
# output
'''
susant 

susant susant 

susant susant susant 

susant susant susant susant 

susant susant susant susant susant '''

# nested for loop
'''
n = 4
for i in range(n):
    for j in range(i,n-1):
        print(" " * len('susant'), end=' ' )
    for j in range(i+1):
        print('susant', end = ' ')
    for j in range(i):
        print('susant', end=' ')
    print()'''
# output
    '''
                     susant 
              susant susant susant 
       susant susant susant susant susant 
susant susant susant susant susant susant susant 
'''

