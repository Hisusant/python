# python basics 
# Python interview questions 
1 . what is the difference between list, tuple, set 
  Answer : 
  1. all 3 are used to store heterogeniuos elements 
  1. list() is mutable( value assignment) - represents l= [1,2,3,3,3,3,4,5,'susant', 33.33,True]
     l.count(2) - it counts how many times 2 occurs in the list, total number of occurance of 2
     l.append(4), l.append([3,4,5,9])- append the element to the list as it is, bedefault add at the last
     l.extend(4) - not work as int value can't iterate, l.extend([23,44,33}) - it will unrap the list and add one by one to the list , 
     l.extend('susant')- it will unrap and add like 's', 'u', 's','a','n','t'
     l.sort()- sorted the list in ascending order, l.sort(reverse=true)- sorted in decending order
     l.index('susant') - return index number of the specific element
     l.pop(5) - remove element based on index, by default removes from the last elements, it is not removes permanently, just removes in the run time
     l.reverse() - return the reverse elements
  3. tuple()- immutable ( can't allow value assignment) - represents t= (1,2,3,4,4,4,4,4,5,'susant', 33.33,True)
  2. set()- it removes duplicate elements and retur nonly unique elements, it removes all duplicate elements in the set() ,
     represents s= {1,2,3,4,5,5,5,5,5'susant', 33.33,True}
  
 2. difference between remove() and discard()
    Answer: 
    1. remove(2) - it remove elements. it will remove the element 2 if it's available in the list else it will return key error if not available there
    2. discard (3333) - it remove elements , it it will remove the element 3333 if it's available in the list else it not return any error
  
 3. what is dict  and hpw it represents 
   Answer :
   1. dict - it reprents in key and value pair that is d = {'name' : 'Susant', 'id':101}, represents = {key,value}
   2. d.keys()- returns only keys 
   3. d.values() - returns only values
   4. d.items() - returns both key and values
   
 4. str - string : it is immutable , can't allow value assignment
 
 
