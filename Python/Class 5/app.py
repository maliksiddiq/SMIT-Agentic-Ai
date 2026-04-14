
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

# !pip install request

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

# import numpy as npmath

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

# print(custom.my_function())


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

def greetings():
   "This is docstring of greetings function"
   greet = 'Hello World!'
   return greet

message = greetings()
print(message)