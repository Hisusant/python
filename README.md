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

PYTHON NOTES: 


------------------------------------------------------------------
 API - Application programming interface 

To communicate between two heterogenious systems, fro example run python code in postman app

- we use flask library for api creation - import flask, request, jsonify
- Flask(__name__)
- route('/api path', methods = ["POST","GET"])
- POST - sending/posting data through body 
- GET - sending/posting data through URL

a = request.json['name'] - input data
return jsonify(str()) - return data 


if __name__ == '__main__':
	app.run(port=5001)
----------------------------------------------------------------

DATABASE - MONGODB:
---------------------
import pymongo
client = pymongo.MongoClient("link...........")
databse = client['database_name']
collection = database['table_name']

collection.insert_one(dict_data) - to insert a json record 
collection.insert_many(list_of_records) - To insert a list of records

collection.update_one()
collection.update_many()

collection.delete_one()
collection.delete_many()

collection.find() - To fetch elements
----------------------------------------------------------------

range() and arange() -

 range() we use in python adn arange() we use in numpy - both functionalities are same

-------------------------------------------------------------------------------

difference between print() and return : 

print() returns elements in str or string types 
return - it returns all elements as it was declared if int then return int , if float then return floar if str then return str


--------------------------------------------------------------------------------

create a new virtual environment: 

go to anaconda admin - conda create -n project2 python == 3.6.9
To activate your virtual environment- conda activate project2
go to anaconda - python -m  pip install django
-pip install jupiter
-conda activate project2
checking python version - python - V
--------------------------------------------------

PYTHON ITERABLE and ITERATORS

lst = [1,2,3,4,5,6] - list is iterables
for i in lst:
	print(i)

by using iter() we can convert it to iterators :
lst2= iter(lst)
next(lst2) - iterate one element at a time , run again to see second element
we can also use for loop to iterate it 
for i in lst2:
	print(i)
	
Basic difference between iterable and iterators : memory initialiazation 
- iterable - initialise the memory for lst
- iterators - not initialise the memory for lst2, it initialise memory for the items that we call 

---------------------------------------------------------------------------------------------------------

**PYTHON ITERATORS and GENERATORS:**

**ITERATOR : **

iter() - to convert a list into iterator
next() - it iterarte one element from the list , if you run again then it ietrate the next element 
use for loop to iterate all elemets from iter(lst)

**GENERATORs :**

- ITERATORS - we use iter() and next() . python iterators much more memory efficient
- GENERATORS-To creat a generator we use function and we use yield keyword to iterate all items , if we use return keyword then it return the first element. generators used to create an iterators. generator execution is first and less memory efficient. 

**ITERATIRS : **

lst = [1,2,3,4,5,6]
for i in lst:
	print(i)
lst2 = iter(lst)
next(lst2)
for i in lst2:
	print(i)

**Generator : **

def fun2(n):
	for i in range(n):
		yield i*i
for i in fun2(5):
	print(i)

-----------------------------------------------------------------------------------------------------------

**FILTER() AND MAP() :**

FILTER() - it rturns the True elements . we can say it filter outs the true elements from the list 
MAP() - it return in True/False , it mapped the elements nad return in True/False 

examples - map() - find out even and odd numbers 

# map()  # find out even and odd numbers
def even_odd(num):
    if num%2==0:
        return "even number: {}".format(num)
    else:
        return "odd number: {}".format(num)
even_odd(3)
even_odd(4)
lst = [12,3,4,5,6,7,8,9]
map(even_odd, lst)  # first paramenter is function name, second is argument 
list(map(even_odd, lst)) # iterate the lements through list 

example - filter()- find out even numbers 
def even(num):
    if num%2==0:
        return "even"
even(10)
even(11)
lst = [2,3,4,5,6,7,8,33,44,55,66,77]
filter(even, lst) # it takes two parameters that are function name and argument
list(map(even,lst)) # iterate the lements through list 

----------------------------------------------------------------------------------------------

**LAMBDA() **

- lambda function or annonimous function / function with no name  # we use incase of we return a single expression
general function : 

def addition(a,b):
    return a+b
addition(3,4)

Lambda function : 

add = lambda a,b:a+b
add(4,6)

------------
even1 = lambda num:num%2==0
even1(11)
-------------
add33 = lambda a,b,c:a+b+c
add33(2,3,44)
----------------------
big = lambda a,b: a if a>b else b
big(2,5)
-----------------------------
big_small = lambda a,b,c : a if a>b and a > c else b if b>c else c
big_small(10,300,100)

----------------------------------------------------------------------------------------------------

**LIST  COMPREHENSION : **

:It provides a concise way to create a list 
it consists of brackets containing an expression followed by a for clause.  if required add more for clause / if clause 

lst2=[]
def square(lst):
    for i in lst:
        lst2.append(i*i)
    return lst2
square([2,3,4,5,6,7])

lst=[1,2,3,4,5,6,7,8]
[i*i for i in lst]  # this is called list comprehension 

# square only even numbers 
[i*i for i in lst if i%2==0]  # adding an if clause

# calculate square of odd numbers 
[i*i for i in lst if i%2!=0]  # adding if clause 

n=5
[n * i for i in range(1,11)]

--------------------------------------------------------------------------------------------

**PYTHON EXCEPTION HANDLING : **

if we do not use exception in our program if any error occured then it will not execute the next line of code. it will stop execution .

if we use exception in our program then it will handle the exception adn run next line of code 

keywords - 

try: block of code where exception may occured 

except: print the user frieldnly message for exception 

else: this block not execute if any exception occured 

finally: this block execute all times either excetion occures or not . if we want to execute some code either exception occured or not then we will write that code in finally block 

raise: we use raise keyword to raise a custom exception as per my requirement 

examples : 
# try exception 
try:
    a = int(input('Enter 1st number: '))
    b = int(input("Enter 2nd number: "))
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    print(add)
    print(sub)
    print(mul)
    print(div)
except NameError:
    print("Enter some value")
except TypeError:
    print("Enter some value")
except ZeroDivisionError:
    print("denominator should be greater than zero")
except Exception as e:  # To catch any other exception 
    print(e)
	
--------------------
# try ----except --- else
try:
    a = int(input('Enter 1st number: '))
    b = int(input("Enter 2nd number: "))
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    
except NameError:
    print("Enter some value")
except TypeError:
    print("Enter some value")
except ZeroDivisionError:
    print("denominator should be greater than zero")
except Exception as e:
    print(e)
else:
    print(add)
    print(sub)
    print(mul)
    print(div)
-------------------------------
# try ----except --- else-----finally
try:
    a = int(input('Enter 1st number: '))
    b = int(input("Enter 2nd number: "))
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    
except NameError:
    print("Enter some value")
except TypeError:
    print("Enter some value")
except ZeroDivisionError:
    print("denominator should be greater than zero")
except Exception as e:
    print(e)
else:        # else block won't execute if any error occured
    print(add)
    print(sub)
    print(mul)
    print(div)
finally:   # finally block execute all time either error occured or not 
    print("This block execute either error occured or not")
---------------------------------------------
# try ----except --- raise , raise - we use to raise an custom exception that we created 

#creating user defined exception

class error1(Exception):
    pass
class dobexception(error1):
    pass

# my requirement - accept age between 20 to 30 years , if > 30 years then raise exception if < 20 years the nreise exception
# raise - To raise a custom defined exception 

try:
    year = int(input("Enter your age: "))
    age = 2022-year
    if age>=20 and age<30:
        print("Your age is {}, you are welcome ".format(age))
    else:
        raise dobexception
except dobexception:
    print("Your age is {}, you are not eligible".format(age))

----------------------------------------------------------------------------------

GITHUB : 

1- donwlaod and install 
2- open cmd and check version :git --version
3- To clear the screen : cls
4- To change the directory : cd C:\Users\dell\Documents\github_mongo
5- To initialise the git : git init
6- To check the files in directory: dir 
7- To check the git global config : git config --global user.name
8- To change the git global config : 
				$ git config --global user.name "spsushanta"
				$ git config --global user.email susant@nexleaf.org

9- To chekc the status : git status
10. To commit files : git commit -m "Thisis my first commit"
11. To know the branch : git branch 

…or create a new repository on the command line
echo "# git_mongodb" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Hisusant/git_mongodb.git
git remote -v
git push origin main

To add files : git add "file_name"
To add all files : git add .

To clone entire repogotory :
		1. create a folder in your system 
		2. go to that folder in command prompt 
		3. clone the repository : git clone https://github.com/Hisusant/git_mongodb.git
		

------------------------------------------------------------------------------------------------

DJANGO and FLASK - web framework for python

Django is a full-stack web framework, whereas Flask is a micro and lightweight web framework. On the other hand, Flask accelerates development of simple web applications by providing the required functionality. Hence, the developers must keep in mind the needs of individual projects while comparing Flask and Django

- creating web application and web APIs 
- Flask framework- especially for data science 
- Django - create very large web application 

- could platforms (Heroko,azure,AWS) for deploying models 

Django instalation and command 
- pip install django
- python -m --version : To check django version , 2.1 or higher is better 
- python - V : To check python version , 3.6 or higher is better 
- django-admin
-> django-admin startproject django_project :  To start the project , give project name 
-> django-admin startapp blog :To create a blog 
-> tree : To check the directory 
-> python manage.py runserver
----------------------------------------------------------------------------------------------------

SnowFlake -

-> python --version
-> pip install --upgrade snowflake-connector-python
-> Test installation : 

Python coding : file name : validate.py

import snowflake.connector

# Gets the version
ctx = snowflake.connector.connect(
    user='<your_user_name>',
    password='<your_password>',
    account='<your_account_name>'
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()

4. Connect to Snowflake
import snowflake.connector
PASSWORD = os.getenv('SNOWSQL_PWD')
conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT
    )
	
------------------------------------------------
command to install all library in one go
-> pip install -r <txt filename>



 
 
