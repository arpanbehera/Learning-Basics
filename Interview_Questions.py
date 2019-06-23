#===============================================
#Q1----------------
# def f(a,b):
#     return (a,b)
#     #return a+b
#
# type(f(1,10))

#Q2--------------

# print("some"+1)

#Q3-----------------
# m = [x,y] for x in range(3),y for y in range(4)
# len(m)

#Q4. Given is the function, what will the call g(2,b=3,c=1) print?
# def g(a=1,b=2,c=3):
#     print("%d,%d,%d" %(a,b,c))
#
# g(2,b=3,c=1)
# g()

#Explaination: The argument values provided in the called function will be taken into account, if nothing is provided then the values with
#defination will be taken into account.

#Q5. What is the result of following statement?
# f = lambda x: sum([i*i for i in range(1,x+1)])
# print(f(5))

# def f(x):
#     #new = []
#     y = 0
#     for i in range(1,x+1):
#         y = i*i + y
#         print(i,y)
#         #new.append(y)
#     print(y)
#
# f(5)

#---------------------------------------

#Q6 In python 2.7 what does the given expression evaluate to?

# print(len(r'1\n2\t3\b'))
# print(len(r'\')) # Error as explained below

'''
r means the string will be treated as raw string

When an 'r' or 'R' prefix is present, a character following a backslash is included in the string without change,
and all backslashes are left in the string.
For example, the string literal r"\n" consists of two characters: a backslash and a lowercase 'n'.
String quotes can be escaped with a backslash, but the backslash remains in the string;
for example, r"\"" is a valid string literal consisting of two characters: a backslash and a double quote;
r"\" is not a valid string literal (even a raw string cannot end in an odd number of backslashes).
Specifically, a raw string cannot end in a single backslash (since the backslash would escape the following quote character).
Note also that a single backslash followed by a newline is interpreted as those two characters as part of the string,
not as a line continuation.
'''
#-----------------------------------
#Q7 What will be the output of the following in python 3?

# a = 4
# b = '8.678'
# c = -5
# str1 = '{0:.4f} {2} {1}'.format(a,b,c)
# print(str1)

'''
{position}.format(value) --> In "format" statement the {} represents the position to be formatted.
str1 is assigned in the sequence {0}{2}{1} from the list of values defined inside format(a,b,c), that's "a' corresponds 0, "b" --> 1 and "c" --> 2.
so str1 = a c b
Again {0:.4f}--> value of variable in 0 position with 4 integer after decimal points. Note: This format is only for floating so "f" is mentioned
'''

#Q8 What is the output for below on interpreter

x = "hi"
x # O/p --> 'hi'
print(x) # O/p --> hi
'''
When the Python interpreter displays the value of an expression, it uses the same
format you would use to enter a value. In the case of strings, that means that it
includes the quotation marks. But if you use a print statement, Python displays
the contents of the string without the quotation marks.
'''