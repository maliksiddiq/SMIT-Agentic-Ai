#  Numeric data Types 
# Python has three main numeric types:

# first_num : int = 15
# print(first_num) 
# print(type(first_num)) 

# sec_num : float = 15.5
# print(sec_num) 
# print(type(sec_num)) 


# third_num : complex = 5 + 3j
# print(third_num)
# print(type(third_num))



# num1 : int = 20
# num2 : float = 10.5

# add : float = num1 + num2
# print(add)

# -----------------------

# integer_val : int = 10
# complex_val : complex = 5 + 3j

# print(f'This is a intger value = ' , integer_val)
# print(f'This is a complex value = ' , complex_val)

# result  = integer_val  + complex_val
# print(f'This is a Final result = ' , result)

# print(f'This is a Real Part = ' , complex_val.real)
# print(f'This is a Imaginary Part = ' , complex_val.imag)

# print(type(complex_val))
# print(type(complex_val.real))
# print(type(complex_val.imag))

# print(5 * 3)
# print(5 + '3') Error
# print(5 * '3') print >>> 33333
# print('5' * 3) print >>> 555
# print(10 * '2' ) Print Two 10 Times

# ---------------------------------------------------------

# Sequence Data Types :
# These store multiple items in an ordered way.

# str1 : str = 'Hello World!'
# str2 : str = "Hello World!"
# str3 : str = '''Hello World!'''
# str4 : str = """Hello World!"""

# print(str1)
# print(str2)
# print(str3)
# print(str4)


# age : str = "I am 20 Year's old"
# print(age)

# text : str = 'They are playing some game"s'
# print(text)

# sentence : str = '''This is a simp"le sentenc'e'''
# print(sentence)


# introduction : str = '''My name is Siddiq i am 20 years old and my 
# profession is Agentic ai Devloper'''
# print(introduction)


# name : str = 'Malik Siddiq'
# print(name)
# print(name[0])
# print(name[1]) 
# print(name[2])
# print(name[3])
# print(name[4]) 

# ---------------------------------------------------

# person_names : list  =  ['Siddiq' , 'Sufiyaan' , 'Aliyaan' ,  'Zaheer' , 'Shadab'] 
# print(person_names)
# print(person_names[0])
# print(person_names[1])
# print(person_names[2])
# print(person_names[3])
# print(person_names[4])

# person_names[2] = 'Ali'
# print(person_names[2])

# --------------------------------------------------

# store_data : list = ['Ahmed ' , 20  , 12.5 , 12+3j , True , 'True' , 'Ahmed']
# print(store_data)
# print(store_data[0])
# print(type(store_data))

# ----------------------------

# is_happy : bool = True
# print(is_happy)
# print(type(is_happy))

# is_lazy : bool = False
# print(is_lazy)
# print(type(is_lazy))

# -------------------------------------------------------

# weekend_name : tuple  = ('Mon' , 'Tue' , 'Wed' , 'Thus' , 'Fri' , 'Sat' , 'sun')
# print(weekend_name)

# weekend_name[0] = 'Monday'   #Error
# print(weekend_name)

# -------------------------------------------------------

# Range (range)

# num_range = range(1 , 10 , 2)
# print(type(num_range) , 'Num range = ' , num_range , num_range.step)


# for i in range(1 , 10 , 2):
#     print(i)

# ----------------------------------------

# my_set : set = {1 , 2 , 3 , 4 , 5  , 5 }
# print(my_set)
# # print(type(my_set))

# my_set.remove(1)
# print(my_set)


# ----------------------------------------

# Frozen Set (frozenset)

# frozen_set = frozenset ([1 , 2 , 3 , 4 , 5 , 5])
# print(frozen_set)
# print(type(frozen_set))


# frozen_set.remove(1)
# print(frozen_set)  #  >>>> Error


# ---------------------------------------------------------------

# Dictionary (dict) Stores key-value pairs.

# person_data : dict = {
#     'name' : 'Haider' ,
#     'age'  : 18 ,
#     'Profession' : 'Devloper' ,
#     'hobbies' : ['Cricket ' , 'Gaming']
# }

# print(person_data)
# print(person_data['name'])
# print(person_data.get('name'))

# ---------------------------------------------

# person_info : dict = {
#     'name' : 'Haider Ali' ,
#     'age' : 20 ,
#     'profession' : 'Devloper' ,
#     'roll_num' : 12345 
# }

# print(person_info)

# person_info['cnic'] = '12342343535'
# person_info['age'] = 22

# del person_info['roll_num']

# print(person_info)

# ------------------------------------------------------------------------

student_data = [
{
    'id' : 1 ,
    'name' : 'Ali' ,
    'age' : 20 ,
    'profession' : 'Devloper' 
} ,
{
    'id' : 2 ,
    'name' : 'Haider' ,
    'age' : 18 ,
    'profession' : 'Designer' 
} ,
{
    'id' : 3 ,
    'name' : 'Hasan' ,
    'age' : 28 ,
    'profession' : 'Programer' 
} ,
{
    'id' : 4 ,
    'name' : 'Ahmed' ,
    'age' : 30 ,
    'profession' : 'VideoEditor' 
} ,
{
    'id' : 5 ,
    'name' : 'Huzaifa' ,
    'age' : 40,
    'profession' : 'Data Scientist' 
} 
]

# print(student_data)
# print(type(student_data))

# print(student_data[0])
# print(student_data[1])
# print(student_data[2])
# print(student_data[3])
# print(student_data[4])


# print(student_data[0].get('name'))
# print(student_data[1].get('name'))
# print(student_data[2].get('name'))
# print(student_data[3].get('name'))
# print(student_data[4].get('name'))

# for student_data_save  in student_data :
#     print(student_data_save)

# ------------------------------------------

# for student_data_save  in student_data :
#     print(f'My name is {student_data_save['name']} and my age is {student_data_save['age']} and my profession is {student_data_save['profession']}')

# ------------------------------------------------------------------------------------ Extra --------------

# check_list  = []
# print(check_list)
# print(type(check_list))

# check_tup = ()
# print(check_tup)
# print(type(check_tup))


# check_set = set()
# print(check_set)
# print(type(check_set))


# check_dict : dict = {}
# print(check_dict)
# print(type(check_dict))


# num = 10 
# print(num)
# print(type(num))  #int


# numbers = 10  , 10 , 10
# print(numbers)
# print(type(numbers))  #tuple


# one_item = (20 ,)
# print(one_item)
# print(type(one_item))

# -------------------------------------------------------------------------------------------------------------------

# String or integer  >>> reuse ho sakte hain
# list or dict hamesha naya object create kre gi  

# Identity operator  (is)

# a : str = 'Hello World!'
# b : str = 'Hello World!'

# print(a is b) #True


# x : str = 'Hello World!'
# y : str = 'Hello World'

# print(x is  y) #False

# ----------------------------------

# num1 : int = 20
# num2 : int = 20

# print(num1 is num2)

# ------------------------------------

# Case 1 (integers):

# integer Interning / Caching Concept   -5 se 256 tk  k integer ik hi memory ko target ke gai 

# a : int= 10
# b : int= 10

# print(a is b)  # True


# x : int = 12000
# y : int = 12000

# print(x is y)

# -------------------------------

# Case 2 (list)

# a = [10]
# b = [10]

# print(a is b)  # False


# ---------------------------------------

# check1 : dict = {
#     'name' : 'Siddiq' ,
#     'age' : 20
# }

# check2 : dict = {
#     'name' : 'Siddiq' ,
#     'age' : 20
# }

# print(id(check1))
# print(id(check2))
# print(check1 is check2)

# ------------------------------------------

# a = [1,2,3]
# b = a
# c = a.copy()

# print(a)
# print(b)
# print(c)

# print(id(a))
# print(id(b))
# print(id(c))

# print(a is b)
# print(a is c)

# -------------------------------------------------------------------

# Membership Operator  >>>> in 

# fruits : list = ['Mango' , 'Apple' , 'Orange' ]
# print(fruits)
# print('Mango' in fruits)
# print('Graphes' in fruits)


# str1 : str = 'Hello World'
# print(str1)
# print('World' in str1) #True
# print('world' in str1) #False

# ----------------------------------------------------- type Casting --------------------------------

# ! Implicit Type

# num1 : int = 10
# num2 : float = 15.5

# result = num1 + num2
# print(result)
# print(type(result))


# --------------------------------------------------------

# ! Explicit Conversion 

# name : str = 'Haider Ali'
# age : int = 18
# profession : str = 'Devloper' 

# intro  = 'My name is ' + name + ' and my age is '  + str(age) +  ' and my profession is ' + profession
# print(intro)


# num_1 = str(10)
# print(num_1) 
# print(type(num_1)) 


# cnic = int('12123425453')
# print(cnic)
# print(type(cnic))

# --------------------------

# cnic = float('12123425453')
# print(cnic)
# print(type(cnic))

# --------------------------

# is_happy = bool('True')
# print(is_happy)
# print(type(is_happy))

# is_lazy = bool('False')
# print(is_lazy) True
# print(type(is_lazy)) bool


# falsy = bool(0)
# print(falsy) False
# print(type(falsy)) bool


# number_1 = bool(0)
# print(number_1)
# print(type(number_1))


# number_2 = int(True)
# print(number_2)
# print(type(number_2))


# number_3 = float(False)
# print(number_3)
# print(type(number_3))


# cnic = int('sadad12123425453')
# print(cnic)
# print(type(cnic))


# name = '10'
# print(name)
# print(type(name))

# change = int(name)
# print(type(change))

# ------------------------------------------------------------------------------------------------------------

