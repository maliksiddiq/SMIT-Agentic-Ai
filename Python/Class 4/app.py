
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

# # split into a list of words
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


