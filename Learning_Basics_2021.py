"""
1.1.1 Program: Add 2 numbers provided by user
"""
#print(int(input("Provide first number:")) + int(input("Provide second number:")))


"""
1.1.2 Program: Create a simple calculator using inputs provided by the user. 
The operations supported is '+','-','*','/'
limitations:
1. It can work for 2 numbers, integers only.
2. 
"""
# calc_input = input("' Provide first number' 'arthimetic operator(+, -, *, /)' 'Provide second number:'")
# if "+" in calc_input:
#     values = str.split(calc_input,"+")
#     print(int(values[0])+int(values[1]))
# elif "-" in calc_input:
#     values = str.split(calc_input, "-")
#     print(int(values[0]) - int(values[1]))
# elif "*" in calc_input:
#     values = str.split(calc_input, "*")
#     print(int(values[0]) * int(values[1]))
# elif "/" in calc_input:
#     values = str.split(calc_input, "/")
#     print(int(values[0]) / int(values[1]))
# else:
#     print("No input")

"""
1.2.1 Program: Basic print the input text
This is a very basic program of printing the text provided by the user
"""
# print(input("provide the input text:"))

"""
1.2.2 Program: print few of the datatypes as input
"""
# print(5     ,6.4,"hi",      [1,2,3])  # this print is without formatting
#
#
# print(5, 6.4, "hi", [1,2,3], sep="\n") # this print is with separator

"""
1.2.3 Program: Basic Calculator function with the input
"""
# calc_input = input("'first number' "
#                    "'arthimetic operator(+, -, *, /)' '"
#                    "second number:'")
# if "+" in calc_input:
#     values = str.split(calc_input,"+")
#     print(int(values[0]), int(values[1]), sep="+", end= "")
#     print('', int(values[0]) + int(values[1]), sep="=")
# elif "-" in calc_input:
#     values = str.split(calc_input, "-")
#     print(int(values[0]), int(values[1]), sep="-", end="")
#     print('', int(values[0]) - int(values[1]), sep="=")
# elif "*" in calc_input:
#     values = str.split(calc_input, "*")
#     print(int(values[0]), int(values[1]), sep="*", end="")
#     print('', int(values[0]) * int(values[1]), sep="=")
# elif "/" in calc_input:
#     values = str.split(calc_input, "/")
#     print(int(values[0]), int(values[1]), sep="/", end="")
#     print('', int(values[0]) / int(values[1]), sep="=")
# else:
#     print("No input")

"""
1.2.3 Program: Printing the path when different sub-folders are known.
"""
print("/","root","basic_python","print_function","Sep_parameter", sep= "/")