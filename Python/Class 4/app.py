
#  ! String

# name : str = 'Malik Siddiq'
# print(name)  


#  ! Four ways to create String 

# single_quotes : str = 'Hello World!'
# double_quotes : str = "Hello World!"
# triple_quotes : str = '''Hello World!'''
# raw_str : str = r'Hel\nlo World!'   # >>> (treats backslashes as literal characters)

# print(f'String with single quotes : {single_quotes}')
# print(f'String with double quotes : {double_quotes}')
# print(f'String with triple quotes : {triple_quotes}')
# print(f'raw string: {raw_str}')


# ! --------------------- Escape Character ------------------

# print("Hello,\b World!") #\b backspace
# print("Hello,\tWorld!")  #\t tab
# print("Hello, \"World!\"")
# print("Hello,\\ World!")
# print("Hello,\n World!")


# ! ------------------------------------------ Basic Opt on string ----------------------------

# str1 : str = 'Hello '
# str2 : str = 'World!'

# concate : str = str1 + str2
# print(concate)


# indexing : str = 'Hello World!'
# print(indexing)
# print(indexing[0])


# slicing : str = 'Hello World!'
# print(slicing)
# print(slicing[0 : 5])


# length : str = 'Hello World'
# print(length)
# print(len(length))


# upper_case : str = 'Hello World!'
# print(upper_case)

# result : str = upper_case.upper()
# print(result)
# print(upper_case)


# lower_case : str = 'HELLO WORLD!'
# print(lower_case)

# result : str = lower_case.lower()
# print(result)
# print(lower_case)


# -------------------------------------------------------------------------

# my_string: str = 'Hello! World'

# # # split into a list of words
# words: str = my_string.split()
# print("my_string.split()    = ", words)
# print(type(words))


# my_string: str = ' , '
# joined_string: str = my_string.join(['Pakistan', 'USA', 'Canada', 'France', 'Japan'])
# print(joined_string)  # Pakistan, USA, Canada, France, Japan



# my_string: str = ' , '
# joined_string: str = my_string.join('Pakistan')
# print(joined_string) 


# countries_name = ' , '
# result = countries_name.join(['Pakistan' , 'Switzerland' , 'Saudia Arabia'])
# print(result)
# print(type(result))



# message : str = 'Hello World! , Hello Everyone!'
# result : str = message.replace('Hello' , 'Hi' )
# print(result)
# print(message)



# my_string: str = "Hello, World! Hello, Pakistan"
# starting_index = my_string.find('Hello')
# print("starting_index = ", starting_index)

# Second 'Hello'  Find

# my_string: str = "Hello, World! Hello, Pakistan"
# starting_index = my_string.find('Hello')
# print("starting_index = ", starting_index)


# starting_index2: str = starting_index  + len('Hello')
# print(my_string[starting_index2:])
# print(my_string[starting_index2:].find('Hello'))


# -----------------------------------------

# my_string: str = "Hello, World! Hello, Pakistan"
# # print(my_string.index('hello')) #Error
# # print(my_string.find('hello')) #-1

# print(my_string.index('Hello' , len('Hello') , len(my_string)))


# my_string : str = 'Hello World , Hello Pakistan'
# check : int = my_string.count('Hello') 
# print(check)
# print(type(check))



# my_string : str = 'Hello World , Hello Pakistan'
# check : int = my_string.count('hello') 
# print(check)
# print(type(check))


# ! ---------------------------------- String Formating --------------

# name : str = "Ali"
# age : int = 20

# print("My name is Ali and I am 20 years old")  #Manually 

# print("My name is {} and I am {} years old".format(name, age))

# print(f'My name is {name} and I am {age} years old')

# --------------------------------------------------------------------------

# name : str = 'Malik Siddiq'
# age : int = 20
# profession : str = 'Devloper'

# print(name , age , profession)
# print(type(name) , type(age) , type(profession))


# using str.format()

# name : str = 'Haider'
# age : int = 20

# my_string: str = 'My name is {} and I am {} years old.'.format(age, name) #order matters
# print("line 1: ",my_string)

# my_string: str = 'My name is {1} and I am {0} years old.'.format(age, name) #use indexing
# print("line 2: ",my_string)

# ! F string

# name : str = 'Haider'
# age : int = 20

# my_string: str = f'My name is {name} and I am {age} years old.' #Using Named Placeholders (Best for Readability)
# print("line 3: ",my_string)


# my_string: str = fr'My \name is {name} and I am {age}\n \t years \old.' #At the same time it could be f and r as well
# print("line 4: ",my_string)


# --------------------------- 

# ! Pool of string literals = Python ka smart system jo same strings ko reuse karta hai taake memory aur speed dono improve ho

# str1 : str = 'Hello'
# str2 : str = 'Hello'
# str3 : str = 'World'
# str4 : str = 'World'

# print(str1)
# print(str2)
# print(str3)
# print(str4)



# a : str = 'Hello'
# b : str = 'Hello'

# print(id(a))
# print(id(b))

# c : str = a + ''
# print(id(c))

# ----------------------------------------

# message1 : str = 'asmdlasmd dfjsdbjfsjdbf sdjf sjd fj sdjf sdfsdf sdfsdf sdfsfgjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj jjjjjjjjjjjjjsdfk  kkkkkkkkks sdfsdfsdfsf'
# message2 : str = 'asmdlasmd dfjsdbjfsjdbf sdjf sjd fj sdjf sdfsdf sdfsdf sdfsfgjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj jjjjjjjjjjjjjsdfk  kkkkkkkkks sdfsdfsdfsf'

# print(id(message1))
# print(id(message2))

# print(message1 is message2)


# str1 : str = 'Hello World'
# str2 : str = 'Hello World'

# print(str1 is str2)

# str1 : str = 'Hello World'
# str2 : str = 'Hello ' + 'World'
# print(str1)
# print(str2)
# print(str1 is str2)



# a = "this is a very long string"
# b = "this is a very long string"
# print(a is b)  # True (interned)
# print("id(a)", id(a))
# print("id(b)", id(b))


# Manual Interning:

# import sys

# str1 : str = sys.intern('Hello World')
# str2 : str = sys.intern('Hello World')

# print(str1 is str2) #True

# str1 : str = sys.intern(['Hello World'])
# str2 : str = sys.intern(['Hello World'])

# print(str1 is str2) # Type error ntern() argument must be str, not list

# ------------------------------------------------------- 

# Get the list of string methods

# string_methods: str = dir(str)
# print(string_methods)

# print('\n')

# x = "hello"
# print(dir(x))

# num = 10
# print(dir(num))

# import math
# print(dir(math))

# ----------------------------------------------------

#using string repetition in a loop.

# String repetition examples

# base_string = "Hello"
# repetition_count = 3

# repeated_string = base_string * repetition_count

# print(f"Original string: {base_string}")
# print(f"Repeated string: {repeated_string}")


# separator = "-" * 30
# print(separator)
# print(type(separator))


# for i in range(1,6):
#   print("*"*i)


# Repeating zero times
# empty_string = "Test" * 0
# print(f"Empty string: '{empty_string}'")



# word = "mango"

# if word > "apple":
#     print(f"{word} comes after apple in alphabetical order")
# else:
#     print(f"{word} comes before apple in alphabetical order")


# word : str = 'Strawberry'

# if word > 'Banana':
#     print(f'{word} comes after Banana in alphabetical order ')
# else:
#     print(f'{word} comes Before Banana in alphabetical order ')


# !  ----------------------------- Type Casting ----------------------------

# num_int: int = 10
# num_float = num_int + 5.5  # int + float = float. skipped type hint to see what data type is assigned at runtime
# print(num_float, type(num_float))


# num_int: int = 7
# num_complex: complex = num_int + 3j  # int + complex → complex
# print(num_complex, type(num_complex))

# num_int automatically promotes int to complex type
# num_int = num_complex
# print(num_int, type(num_int))


# num_float: float = 9.8
# num_int = int(num_float) # skipped type hint to see what data type is assigned at runtime
# print(num_int, type(num_int))


# b: bool = True
# print("int(b) = ", int(b))


# lst: list = [("name", "Alice"), ("age", 25)]
# print(lst , type(lst))
# d  = dict(lst)       # skipped type hint to see what data type is assigned at runtime
# print(d, type(d))


# num: int = 5
# comp = complex(num)   # skipped type hint to see what data type is assigned at runtime
# print(comp, type(comp)) 


# float_num : float = 5.5
# print(float_num , type(float_num))

# convert : complex = complex(float_num)
# print(convert , type(convert))

# change =  str(convert)
# print(change , type(change))


# num : int = 5
# compl  : complex = complex(num)
# print(compl , type(compl))


# compl : complex = 5 + 3j
# print(compl , type(compl))

# convert = int(compl)
# print(convert  , type(convert))

# a : int = int('10')
# print(a , type(a))

# b : float = float('10')
# print(b , type(b))


# num : str = str(10)
# print(num  , type(num))
# print(num  + '10' , type(num))


# set_1  = set([1 , 2 , 3 , 3 , 4 , 5 , 6 , 5 ])  
# print(set_1 , type(set_1))


# list_1 = list({1 , 2 , 3 , 4 , 5 , 5 , 6 , 7})
# print(list_1 , type(list_1))

# print(list_1[0])


# cnic =tuple(['1232435546' , '133245456576' , '1232445345466'])
# print(cnic , type(cnic))

# cnic[0] = '1111111111233'
# print(cnic , type(cnic))


# student_data = dict([('name ' , 'Siddiq') , ( 'age' , 20) , ('profession' , 'Devloper')])
# print(student_data  , type(student_data))

# print(student_data)
# print(student_data['name ']


# -----------------------------------------------


# a = bool('')
# print(a , type(a))

# b = bool('False')
# print(b , type(b))


# b = 'False'  == 'True'
# print(b , type(b)) 


# user_input : str = 'False'
# print(user_input , type(user_input))
# save : bool = user_input.lower()  == 'true'
# print(save , type(save))


# num : int = 10
# print(num  , type(num))
# compl : complex = 5 + 3j
# print(compl , type(compl))


# add : complex = num + compl
# print(add , type(add))


# s = "python"
# print(s[::-1])



