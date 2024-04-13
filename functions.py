# Functions
# Its a buch of code which performs a 
# particular task and is called when 
# it's about be used


# def greetingd_function(name, age):
#     print('Welcome '+name+ ' and you are '+str(age)+' years old')

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# greetingd_function(name, age)

# Lets now learn how to use the return keyword 
# in python which gives an output of what is been 
# executed



# def greet(name):
#     print('Welcome ' + name)
# greet('Raoul')


# def my_function():
#     return 4+6
# print(my_function())




# Lets write a function which add 2 numbers with return


def add_numbers(number1, number2):
    print('Always true know where the function is valid')
    return number1 + number2

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
print(add_numbers(number1, number2))