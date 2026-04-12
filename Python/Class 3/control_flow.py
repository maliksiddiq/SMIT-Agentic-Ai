
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

# ------------------------------------------------------------------------------------

# def check_status(code):
#     match code:
#         case  200:
#             print("OK")
#         case    400:
#             print("Bad Request")     
#         case   404:
#             print("Not Found")
#         case _:
#             print("Unknown Status")


# check_status(200)    
# check_status(400)    
# check_status(404)    
# check_status('_')    


# ------------------------------------------------------------------------------------

# fruits : list = ['Apple' , 'Banana' , 'Orange' , 'Strawbeery']

# for fruit in fruits:
#     print(fruits)

# word: str = "Python"
# for letter in word:
#     print(letter)


# --------------------------------------------- Loops Wih else Block ----------------

# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     print(num)
# else:
#     print("Loop completed successfully!")


# ------------------------------------------ break ---------------

# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     print(num)
#     if num == 3:
#         print("Breaking the loop!")
#         break
# else:
#     print("Loop completed successfully!")  # This will NOT run

# -------------------------------------------------

# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     if num == 6:
#         print("Number found!")
#         break
# else:
#     print("Number not found!")  # Runs because 6 is not in the list


#  -------------------------------------------------

# for i in range(5):
#     print(i)

# for i in range(2 , 11 , 2):
#     print(i)

#  ! -------------------------------------------------throway Variable _ temporary variable --------------------

# !  _ “Mujhe ye value mil rahi hai, lekin mujhe iski zarurat nahi hai.”

# for _ in range(5):
#     print(f'Hello')


# for i in range(5):
#     print(i , 'Hello World!')
    

# for _ in range(10):
#     print(f"Hello, World! Iteration { _ }")


# ! ------------------------------------ While Loop -----------------------------

# count: int = 1
# while count <= 5:
#     print(count)
#     count += 1


# ! ------------------------------------------------ Break and Coninue ---------------------

# for i in range(10):
#     if i == 5:  
#          break     
#     print(i)  


# for i in range(5):
#     if i == 3:
#         continue
#     print(i)  # Prints 0, 1, 2, 4


# ! ----------------------------------------- Nested Loops ! ------------------------

# for outer in range(1 , 6):
#     print(f'Muliplication table for {outer} :')
#     for inner in range(1 , 6):
#         print(f'{outer} * {inner} = {outer * inner}')
#     print()


# -----------------------------------------------------------

# total: int = 0
# for i in range(1, 101):
#     total += i
# print("Sum of numbers from 1 to 100:", total)    


# num: int = 24
# factors = []
# for i in range(1, num + 1):
#     if num % i == 0:
#         factors.append(i)
# print(f"Factors of {num}: {factors}")