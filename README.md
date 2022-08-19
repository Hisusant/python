# python basics 
# Python interview questions 
1 . what is the difference between list, tuple, set 
   
  1. all 3 are used to store heterogeniuos elements 
  1. list() is mutable( value assignment) - represents l= [1,2,3,3,3,3,4,5,'susant', 33.33,True]
   
     l.count(2) - it counts how many times 2 occurs in the list, total number of occurance of 2
     
     l.append(4), l.append([3,4,5,9])- append the element to the list as it is, bedefault add at the last
     
     l.extend(4) - not work as int value can't iterate, l.extend([23,44,33}) - it will unwrap the list and add one by one to the list , 
     
     l.extend('susant')- it will unwrap and add like 's', 'u', 's','a','n','t'
     
     l.sort()- sorted the list in ascending order, l.sort(reverse=true)- sorted in decending order
     
     l.index('susant') - return index number of the specific element #
     
     l.pop(5) - remove element based on index, by default removes from the last elements, it is not removes permanently, just removes in the run time
     
     l.reverse() - return the reverse elements
     
  3. tuple()- immutable ( can't allow value assignment) - represents t= (1,2,3,4,4,4,4,4,5,'susant', 33.33,True)
  
  5. set()- it removes duplicate elements and retur nonly unique elements, it removes all duplicate elements in the set() ,
     represents s= {1,2,3,4,5,5,5,5,5'susant', 33.33,True}
  
 2. difference between remove() and discard()

    1. remove(2) - it remove elements. it will remove the element 2 if it's available in the list else it will return key error if not available there
    2. discard (3333) - it remove elements , it it will remove the element 3333 if it's available in the list else it not return any error
  
 3. what is dict  and hpw it represents 

   1. dict - it reprents in key and value pair that is d = {'name' : 'Susant', 'id':101}, represents = {key,value}
   2. d.keys()- returns only keys 
   3. d.values() - returns only values
   4. d.items() - returns both key and values
   
 4. str - string : it is immutable , can't allow value assignment
 
 **FUNCTIONS : **

1. a,b,c,d = test() # fundction call # test() returns 4 elements and each element stored in each variable

2. _,_,_, d = test()  # function call -> #  _,_,_,  this (underscore) is called placeholders , test() returns 4 elements but i want only one element that is d

3. difference between print() and return 

   1. print() - it returns Nonetype as data types 
   2. return - it returns the datatypes as it is *(declared) , not change the data types of the variable
      
4. 
 
 
EXCEPTION HANDLING : Handling run time error is called exception handling

 code flow :  source code -> compiler( here we get syntax error) -> byte code/machine code -> interpreter ( here we get run time error)
 
 error : 
   1. compile time error - syntax error are known as compile error
   2. run time error - handling run time error is know as exception handling
 
 why we use exception in our program ? 

    1- Handling run time error if not do then it will not execute next line of code. 
    2. if we use exception handling , if any error occures during run time then it will handle the error and execute all codes
    3. if we don't use exception, if error occures then it will not execute next line of code, it will stop there where exception occures. 
    
  There are 5 keywords that are : 
     try :
      block of code...
     except:
      block of code
     raise:
      block of code
     finally:
      block of code
     else:
      block of code
      
  
 NUMPY : 
 np.random(100)--- generate random numbers in between 0 to 100
 
 np.random.rand(100,3)-- create postitives floting number
 
 np.random.randn(100,3) -- creates negetive floating numbers

 
 
