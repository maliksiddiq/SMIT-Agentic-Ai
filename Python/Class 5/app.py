
#  ! Module  and Functions 

# ! Built in module 

# import math

# print(math.sqrt(25)) #5.0
# print(math.sqrt(16)) #4.0
# print(math.sqrt(36)) #6.0

# print(dir(math))
# print('\n')
# print(math.pi)


# ! Custom Module 

# import custom

# ! add 

# print(custom.add(10 , 20))
# print(custom.add(50 , 20))

# ! sub

# print(custom.sub(20 , 10))
# print(custom.sub(40 , 10))

# ! mul

# print(custom.mul(10 , 10))
# print(custom.mul(100 , 100))


# !Third Party Module

# pip install request

# import requests

# print(requests.__version__)

# response = requests.get("https://www.example.com")
# print(response.status_code)
# print(response.content)


# ! Import Module 

# 1. Basic Import

# import math

# print(math.sqrt(25)) #5
# print(math.pi) 


# ! 2 Import with Alias (as)

# import numpy

# print(numpy.__version__)

# import numpy as np

# print(np.array([1, 2, 3]))


# import custom as  c

# print(c.add(10 , 10))


# ------------------------------------------------------
# import math

# print(math.sqrt(16)) #4
# print(math.pi)
# print(math.ceil(4.6)) 
# print(math.ceil(4.1)) 
# print(math.ceil(-4.1)) 
# print(math.ceil(4)) 
# print(-4.1 < -4)

# print(math.floor(6.3))

# print(dir(math))


# from math  import  sqrt , pi 

# print(sqrt(25)) #5
# print(pi) #5


# from math import sqrt as s, pi as p

# print(s(25))
# print(p)


# ------------------------------------------------

# from math import * # wild card
# print(sin(0))

# import math

# -----------------------------------------------

# from math import *
# from numpy import *
# print(pi)

# ! ------------------------------ nameSpace managment -------- >>> onflicts se bachana

# x = 10   # global variable

# def my_func():
#     x = 5   # local variable
#     print(x)

# my_func()
# print(x)

# ------------------------------------------------------------

# def my_function():
#   print("Hello! World")

# my_function()
# my_function()
# my_function()


# import custom

# custom.my_function()

# custom.outer_func()
# custom.inner_func()


# def outer_func():
#     print('Outer Function')
#     def inner_func():
#         print('Inner function')
#     inner_func()
#     inner_func()

# outer_func()


# x = 10

# def var():
#     x = 20
#     print(x)
# print(x)

# var()
# print(x)


# !Types of functions

#  ! Built-in functions
# print("Hello! World")


# ! Functions defined in built-in modules

# import random
# print(random.random())

# ! User-defined functions

# def my_function():
#   print("Hello! Operation Badar")

# my_function()  


# --------------- Function Syntax --------

# def greetings():
#    "This is docstring of greetings function"
#    greet = 'Hello World!'
#    return greet

# # greetings()

# message = greetings()
# print(message)


# -------------- Pass By refernce vs value -------- 

# def modify_value(x):
#     x = 10
#     print("Within function:", x)

# # Immutable object (integer)
# x = 5
# print("Original:", x)
# modify_value(x)
# print("After function:", x)


# ---------------------------------- Function argument ---------------

# def greet(name):
#     print('Well Come to our Website! ' , name)

# greet('Haider Ali')
# greet('Hamza')
# greet('Ali')
# greet()


# def intro(name , age , profession):
#     print(f'My name is {name} and i am {age} Years old and i am a {profession}') 

# intro('Siddiq' , 20 , 'Devloper')    
# intro('Haider Ali' , 18 , 'Designer')    
# intro('Mazhar Ali' , 25 , 'Programer')    



# def intro(name , age , profession):
#     print(f'My name is {name} and i am {age} Years old and i am a {profession}') 

# intro(20 , 'Siddiq' , 'Devloper')    
# intro(18 , 'Haider Ali' , 'Designer')    
# intro( 25 , 'Mazhar Ali' , 'Programer')   


# def greetings(name):
#    "This is docstring of greetings function"
#    print ("Hello {}".format(name))
#    return

# greetings("Ali")
# greetings("Omar")
# greetings("Usman")

# ! ------------------------ 


# def intro(name , age , profession):
#     print(f'My name is {name} and i am {age} Years old and i am a {profession}') 

# intro(age=20 , name='Siddiq' , profession='Devloper')    
# intro(age=18 , name='Haider Ali' , profession='Designer')    
# intro(age=25 , name='Mazhar Ali' , profession='Programer')   

# ----------------------------------- Error Solve -----------------------

# def intro(name , age , profession):
#     print(f'My name is {name} and i am {age} Years old and i am a {profession}') 

# intro(age=20 , name='Siddiq' , 'Devloper')   #Error 
# intro(age=18 , name='Haider Ali' , 'Designer')   #Error 
# intro(age=25 , name='Mazhar Ali' , 'Programer')  #Error


# intro('Siddiq' , profession= 'Devloper' , age= 20)    
# intro('Haider Ali', profession= 'Designer' , age=18)    
# intro('Mazhar Ali' , profession= 'Programer' , age=25)  

# ---------------------------------------------------------------------------------------

# def add(x: int,y: int=0) -> float:
#    return float(x + y)

# print(float(add(10,20)))

# print(add(y=50.0, x=2.0)) # type hints are not enforced in Python

# print(add(x=5))


# ---------------------------------------------------------------------------------------

# ! Packing 

# def func(*nums):
#     print(nums , type(nums))

# func(1, 2, 3, 4) 


# ! Unpacking 

# nums = (1, 2, 3)

# a, b, c = nums
# print(a, b, c)


# def store_list(num): #Error   
#     print(f'The value is {num} and its type is {type(num)}')

# store_list(*[1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]) #unpackng
# store_list(*(1 , 2 , 3 , 4 ,5)) #unpackng


# def store_list(*num): #Solve the error   
#     print(f'The value is {num} and its type is {type(num)}')

# store_list(*[1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]) #unpackng
# store_list(*(1 , 2 , 3 , 4 ,5)) #unpackng


# def store_lists(*num):   
#     print(f'The value is {num} and its type is {type(num)}')

# store_lists(*[1 , 2, 3 , 4] , [5 , 6 , 7 , 8 , 9 , 10])
# store_lists(*(1 , 2, 3 , 4) , (5 , 6 , 7 , 8 , 9 , 10))


# def func(**student_data):
#     print(f'The value is {student_data} and its type is {type(student_data)}')

# func(first_name = 'Haider' , last_name = 'Ali') #as a dict data type
# func(first_name = 'Haider' , last_name = 'Ali' , cnic = 123134342 , profession = 'Devloper')


# def create_user(*data):
#     print(data)

# user_data = {
#     "name": "Siddiq",
#     "age": 20,
#     "city": "Karachi" 
# }

# create_user(*user_data) #('name', 'age', 'city')

# def create_user(**data):
#     print(data)

# user_data = {
#     "name": "Siddiq",
#     "age": 20,
#     "city": "Karachi" 
# }

# create_user(**user_data) #{'name': 'Siddiq', 'age': 20, 'city': 'Karachi'}


# def store_data(data):
#     print(data)


# student_info : dict = [
# {
#      'name' : 'Siddiq' ,
#      'age' : 20 ,
#      'profession' : 'Devloper'  
    
#  } ,
# {
#     'name' : 'Haider' ,
#      'age' : 18 ,
#      'profession' : 'Designer'  
# } 
# ]

# print(student_info)
# print(student_info[0])
# print(student_info[1])

# store_data(student_info)



# Error in This Code 
# store_lists(*{'name' : 'Haider Ali' , 'age' : 18 , 'Profession' : 'Devloper'} , {'name' : 'Siddiq' , 'age' : 20})