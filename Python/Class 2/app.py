
#!  Negative Unary Operator

# x = 5
# y = -x   

# print(x)
# print(y)

# print(-5)

# ! Logical Not Unary Opearator 

# print(not True , type(True))
# print(not False , type(True))

# bool_val : bool = True
# print(not bool_val) 


# a = True
# b =  not a

# print(a)
# print(b)

# print(a is b)


# ! Bitwise Operation ~

# x : int = 5   # Binary: 0101
# y : int = ~x  #1010

# print(x)
# print(y)

# print(x is y)


# ------------------------------------------------------------------------------------------------------------------------------------

# !. Arithmetic Operators

# print(2 + 2)

# num1 : int = 2
# num2 : int = 2

# result : int = num1 + num2
# print(result)


# print(5 - 3)

# num1 : int = 5
# num2 : int = 3

# result : int = num1 - num2
# print(result)


# print(2 + 2)
# print(5 - 3)
# print(5 * 5)  
# print(12 /  3) #12.0

# print(5 / 2)
# print(5 // 2)

# print(5 % 2)
# print(2 ** 5) 

# ----------------------------------------------------------
# ! . Comparison (Relational) Operators

# print(5  ==  5)

# num_1 : int = 5
# num_2 : int = 5

# result : int = num_1 == num_2
# print(result)


# print(5  ==  5)
# print(5  !=  3)
# print(5  >  3)
# print(2  <  3)
# print(2  <=  2)
# print(5  >= 5)

# ----------------------------------------------------------------------------

# x : int = 15

# if 10 < x < 20 :
#     print('x is between 10 and 20 ')

# if 10 < x and x < 20:
#     print("x is between 10 and 20")


# ! . Logical Operators

# print(True  and  True and True  and True and True  and  True and True  and True )  #True
# print(False  and  True and True  and True and True  and  True and True  and True )  #False

# print(False or True) #True
# print(False or False or False or False or True)

# print(False or False or False or False or  False) #False 
# print(False or False or False or False or not False) #True


# print(5 < 10  and  5 > 2)
# print(5 < 10  and  5 > 10)

# print(10 < 20  or  10 > 5)
# print(10 < 20  or  10 < 5)
# print(10 > 20  or  10 < 5)

# -------------------------------------

# x: bool = True
# y: bool = False

# print("x and y = ", x and y)  # False
# print("x or y  = ", x or y)   # True
# print("not x   = ", not x)    # False

# ------------------------------------------------------------------------------------------------

# !  Assignment Operators

# num : int = 10
# print(num)

# ! Why we use assignment opt 

# x : int = 5
# print(x)

# x = x + 10
# print(x)

# x += 10
# print(x)


# num_1 : int = 2
# print(num_1)

# num_1 *= 2
# print(num_1)

# ------------------------------------------------------------------------------------------------------

# !  Identity Operators

# a : list = [1 , 2 , 3]
# b : list = [1 , 2 , 3]
# c : list = a

# print(a is b) #False
# print(a is c) #True

# print(a == b) #True
# print(a == c) #True

# print(id(a))
# print(id(b))
# print(id(c))


# person_data_1 : dict = {
#     'name' : 'Siddiq',
#     'age' : 20,
#     'profession' : 'Devloper'
# }

# print(person_data_1)

# person_data_2 : dict = {
#     'name' : 'Siddiq',
#     'age' : 20,
#     'profession' : 'Devloper'
# }

# print(person_data_2)

# print(person_data_1 is person_data_2) #False
# print(id(person_data_1))
# print(id(person_data_2))


# num_1 : int = 10
# num_2 : int = 10

# print(num_1 is num_2)
# print(id(num_1))
# print(id(num_2))

 
# str1 : str = 'Hello World!' 
# str2 : str = 'Hello World!' 

# print(str1 is str2)
# print(id(str1))
# print(id(str2))

# bool_1 : bool = True 
# bool_2 : bool = True 

# print(id(bool_1))
# print(id(bool_2))

# print(bool_1 is bool_2)


# tup1 : tuple  = (1 , 2, 3)
# tup2 : tuple  = (1 , 2, 3)

# print(id(tup1))
# print(id(tup2))

# print(tup1 is tup2)

# -------------------------------------------------

# ! . Membership Operators

# fruits : list = ['Mango' , 'Strawberry' , 'Apple']
#  print(fruits)
# print('Mango' in fruits) #True
# print('Cherry' not in fruits) #True
# print('mango' in fruits) #False

# -------------------------------------------------

# x ,  y , z = 10 , 20 , 30
# print(x)  
# print(y)  
# print(z)  

# print(x , y , z)

# ------------------------------------------ del keyword ---------------------

# x : int = 10

# del x
# print(x)

