
# ! Control Flow

# “The order in which instructions (code) are executed in a program.”

# ! Default Flow

# print("Start")
# print("Learning Python")
# print("End")

# ----------------------------------

# age : int = 25
# is_student : bool = True

# if age > 18 and is_student == True:
#     print('You are eligible for a student discount.')
# else:
#     print('You are not eligible for a student discount')    

# ----------------------------------------

# age : int = 10
# if age < 12 or age > 60:
#     print("You qualify for a special discount.")

# ----------------------------------------

# num : int = 10

# if num > 0:
#     print('Positive Number!')
# else:
#     print('Negative Number!')    

# --------------------------------------------------------

# num: int = -5

# if num > 0:
#     print("The number is positive.")
# else:
#     print("The number is not positive.")

# --------------------------------------------------------

# num: int = 0

# if  num > 0:
#     print('The number is Positive!')
# elif num < 0:
#     print('The number is Nagative!')    
# else:
#     print('The number is Zero!')

# ! -------------------------------------------------------- Trafiic Signal System ------------------------------

# light : str = 'Green'

# if light == 'Red':
#     print('Stop!')
# elif light == 'Yellow':
#     print('Wait!')   
# elif light == 'Green':
#     print('Go!')
# else:
#     print('Light is Damage!')    

# ------------------------------------------- Nested Conditional Statement -----------------------------------

# num: int = -11

# if num > 0: # check wather the number is positive or negative

#     if num % 2 == 0: # Modulus operator, remainder 0 = even_number,
#         print("The number is positive and even.")
#     else: # remainder 1 = odd_number,
#         print("The number is positive and odd.")

# else:
#     print("The number is negative.")

# --------------------------------------------------------------------------------------

# ! input

# user_name = input('Enter a name :')
# print(f'This is a Value of User_name Variable : {user_name}')


# num1 = int(input('Enter a First Number! :'))
# num2 = int(input('Enter a Sec Number! :'))

# result = num1 + num2
# print(result)

# ------------------------------------------------------------------------------------------------

# operation: str = input("Enter the operation (+, -, *, /): ") 

# num1: float = float(input("Enter the first number: "))
# num2: float = float(input("Enter the second number: "))

# if operation == '+':
#     result = num1 + num2
# elif operation == '-':
#     result = num1 - num2
# elif operation == '*':
#     result = num1 * num2
# elif operation == '/':
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error: Division by zero."
# else:
#     result = "Invalid operation."

# print("Result:", result)