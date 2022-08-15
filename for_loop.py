#l = [1,2,3,4,"susant" ,"kumar" , 45.56]
# print the list of item in for loop
'''for i in l:
    print(i)
'''
# for loop with else blocl
'''for i in l:
    print(i)
else:
    print("else block")
'''
# use of pass in for loop
'''for i in l:
    pass
'''
# extract each letter from the name
'''name = 'sushanta'
for i in name:
    print(i)
'''

# print only integer from the list by using break
l = [1,2,3,4,"susant" ,"kumar" , 45.56]
for i in l:
    if (i=='susant'):
        break
    print(i)
else:
    print("else block")  # else block won't be execute if we use break

