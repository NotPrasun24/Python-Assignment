# name = input("Hello, what is your name? ")
# print(f"Hello Mr {name}. Good to meet you! ")


# celsius = float(input("Enter a temperature in Celsius: "))
# fahrenheit = celsius * (9 / 5) + 32
# print(f"{celsius}C is equivalent to {fahrenheit}F") 




# students = int(input("How many students are there? "))
# groups = int(input("What is your requied group size? "))

# num_groups = students // groups
# leftovers = students % groups 

# print(f"There will be {num_groups} groups with {leftovers} students left over. ")



# sweets = int(input("Enter how many sweets: "))
# pupils = int(input("Enter how many pupils: "))

# distrubutions = sweets//pupils

# print(distrubutions)






# Modify your greeting program so that if the user does not enter a name (i.e. they
# just press enter), the program responds "Hello, Stranger!". Otherwise it should print
# a greeting with their name as before.


# name = input("Enter your name: ")
# if name == "":
#     print("Hello, Stranger!")
# else:
#     print("Hello, "+ name)




# Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again. If the two
# passwords entered are the same the program should say "Password Set" or
# similar, otherwise it should report an error.


# password = input("Set your password: ")
# print("Password has been saved! ")
# guess = input("Enter your password: ")
# if guess == password:
#     print("Access granted!")
# else:
#     print("Access denied!")



# Modify your previous program so that the password must be between 8 and 12
# characters (inclusive) long.


# password = input("Set your password between 8-12 letters: ")
# # print("Password has been saved! ")
# if len(password) >= 8 and len(password) <= 12:
#     guess = input("Enter your password: ")
#     if guess == password:
#         print("Password Set!")
#     else:
#         print("password doest match ")
    
# else:
#     print("Password must be between 8-12 letters")




# Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
                                                         

# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# password = input("Set your password between 8-12 letters: ")
# if len(password) >= 8 and len(password) <= 12 and password not in BAD_PASSWORDS:
#     guess = input("ReEnter your password: ")
#     if guess == password :
#         print("Password Set!")
#     else:
#         print("password doest match ")
# elif password in BAD_PASSWORDS:
#     print("COmmon password, Try again")
# else:
#     print("Password must be between 8-12 letters")




# Modify your program a final time so that it executes until the user successfully
# chooses a password. That is, if the password chosen fails any of the checks, the
# program should return to asking for the password the first time.



# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
# while True:    
#     password = input("Set your password between 8-12 letters: ")
#     if len(password) >= 8 and len(password) <= 12 and password not in BAD_PASSWORDS:
#         guess = input("ReEnter your password: ")
#         if guess == password :
#             print("Password Set!")
#             break
#         else:
#             print("password doest match ")
#     elif password in BAD_PASSWORDS:
#         print("COmmon password, Try again")
#     else:
#         print("Password must be between 8-12 letters")




# Write a program that displays the "Seven Times Table". That is, the result of
# multiplying 7 by every number from 0 to 12 inclusive. The output might start:
# 0 x 7 = 0
# 1 x 7 = 7
# 2 x 7 = 14
# and so on.

# a = 0 
# while a <= 12:
#     print(f"{a} x 7 = {a * 7}")
#     a += 1




# Modify your "Times Table" program so that the user enters the number of the table
# they require. This number should be between 0 and 12 inclusive.


# a = 0
# while True:
#     user_number = int(input("Enter your number: "))
#     if 0 <= user_number <= 12:
#         while a <= 12:
#             print(f"{a} x {user_number} = {a * user_number}")
#             a += 1
#             break
#     else:
#         print("ERROR!, Please enter a number between 1 to 12 only")
       





'''Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times". '''


# b = 12
# a = 0
# while True:
#     user_number = int(input("Enter your number: "))
#     if 0 <= user_number <= 12:
#         while a <= 12:
#             print(f"{a} x {user_number} = {a * user_number}")
#             a += 1
#         break
#     elif user_number < 0:
#         while b >= 0:
#             print(f"{b} x {user_number} = {b * user_number}")
#             b -= 1
#         break
#     else:
#         print("ERROR!, Please enter a number less than 12")












# WEEK 4


'''Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function.'''

# def check(n):
#     if n >= 0 and n <= 100:
#         return True
#     else:
#         return False
# print(check(0))



'''Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program.'''


# def check_string(n): 
#     uppercase = sum(1 for a in n if a.isupper())
#     lowercase = sum(1 for a in n if a.islower())

#     return uppercase, lowercase
 
# uppercase,lowercase = check_string("PrAsUn SeDAi")
# print(f"The uppercase letters is: {uppercase}")
# print(f"The lowercase letter is: {lowercase}")






'''Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name dierently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur.'''


# def capital(name):
#     return name.capitalize()
# name = input("Enter your name: ")
# if name == "":
#     print("Hello, Stranger!")
# else:
#     print(f"Hello, {capital(name)}. Good to meet you.")


'''When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.)'''


# def remove_last_character(word):
#     if len(word) <= 1:
#         return word
#     else:
#         return word[:-1]
# print(remove_last_character("Prasun"))



'''Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae).'''


# def celcius_to_fahrenheit(celcius):
#     return ((celcius * 9/5) + 32)
# def fahrenheit_to_celcius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# print(f"{celcius_to_fahrenheit(0)}F")
# print(f"{fahrenheit_to_celcius(32)}C")



'''Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format.'''



# def celcius_to_fahrenheit(celcius):
#     celcius = float(celcius[ :-1])
#     return ((celcius * 9/5) + 32)
# def user_input():
#     user_input = input("Enter temperature in celcius followed by C (example 32C): ").upper()
#     return user_input

# def test():
#     user = user_input()
#     fahrenheit_tempreture = celcius_to_fahrenheit(user)
#     print(f"{user} is equal to {fahrenheit_tempreture}F")

# test()









'''Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean.'''


def celcius_to_fahrenheit(celcius):
    celcius = float(celcius[ :-1])
    return ((celcius * 9/5) + 32)


def user_input():
    for i in range(6):
        user_input = input("Enter temperature in celcius followed by C (example 32C): ").upper()
    return user_input

def test():
    user = user_input()
    fahrenheit_tempreture = celcius_to_fahrenheit(user)
    print(f"{user} is equal to {fahrenheit_tempreture}F")

test()





