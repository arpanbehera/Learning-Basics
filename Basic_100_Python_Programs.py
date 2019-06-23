"""
List of programs in this project:
22-06-2019:
    Program 1: Find numbers divisible by 1 number and not divisible by another with output string comma separated
    Program 2: Making mirror image(complete reverse of the string)
        Program 2.1: Using String slicing
        Program 2.2: Generic Procedural statements with list
        Program 2.3: Using Function
        Program 2.4: Using function and List comprehension
        Program 2.5: Using decorators
    Program 3: Making mirror image of the words"
        Program 3.1: Generic Procedural statements
        Program 3.2: Using function and list comprehension
        Program 3.3: Using List slicing and list comprehension
    Program 4: Making mirror image of independent - Words position remains same but elements inside each words is reversed"
        Program 4.1: Generic Procedural statements
        Program 4.2: using function
        Program 4.3: Using string slicing Function and List comprehension
    Program 5: Combination of program 4, program 3 and program 2
    Program 6: Find the duplicate characters in a string
        Program 6.1: Using general procedural statements and list
        Program 6.2: Using general procedural statements with strings
        Program 6.3: Using Functions and count module of string
        Program 6.4: Using Functions and count module of string with list comprehension
        Program 6.5: Using function and dictionary
    Program 7: Find the duplicate words in a string
        Program 7.1: Using general procedural statements
        Program 7.2: Using string count for identifying duplicate characters
        Program 7.3: Using Function and Dictionaries
    Program 8: Find the word in pairs which are repeated in a file. Also should remove any special characters in the words.
    Program 9: Password check validation
        Program 9.1: Using string inbuilt function
        Program 9.2: Using converting the values to ascii and verifying criteria
    Program 10: Calculate the length of a string without any function
    Program 11: Count the number if character in a string/file
        Program 11.1: Using string count function and dictionary
    Program 12: Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
    Problem 13: Convert numbers base 8(Oct-decimal), base 16(Hexadecimal), base 2(Binary) to Int base 10(decimal)


"""

print("----*****hello Arpan these are all basic programs written*****-----")


#=============================================================================================================
#Program 1: Find numbers divisible by 1 number and not divisible by another with output string comma separated
#=============================================================================================================
'''
output = []
#output = " "
for number in range(2000,3201):
    if number % 7 == 0 and number % 5 != 0:
        #output = str(number) + "," + output
        output.append(str(number))

print(",".join(output))
'''

#=============================================================================================================
# Program 2: Making mirror image(complete reverse of the string)
# input: "Reverse me"
# Output: "em esreveR"
#=============================================================================================================

#-------------------------------------------------------------------------------------------------------------
# Program 2.1: Using String slicing
#-------------------------------------------------------------------------------------------------------------
'''
print(input("Provide your input string:")[::-1])

'''

# -----------------------------------------------------------------------------------------------------------
# Program 2.2: Generic Procedural statements with list
# -----------------------------------------------------------------------------------------------------------
'''
Input_string = "Reverse me"
str_to_reverse=list(str(Input_string))
#print(str_to_reverse)
Reversed_str = []
for x in range(len(str_to_reverse)-1,-1,-1):
     Reversed_str.append(str_to_reverse[x])
print("".join(Reversed_str))

'''
#-----------------------------------------------------------------------------------------------------------
# Program 2.3: Using Function
# ----------------------------------------------------------------------------------------------------------
'''
def Reverse_string(Input_str):
    Input_string_list = list(Input_str)
    Reversed_str_list = []
    for elements in range((len(Input_string_list)-1),-1,-1):
        Reversed_str_list.append(Input_string_list[elements])
        Reversed_str = "".join(Reversed_str_list)
        return Reversed_str

Output_string = Reverse_string(input("Provide your input string:"))
print(Output_string)
'''
# ----------------------------------------------------------------------------------------------------------
# Program 2.4: Using function and List comprehension
# ----------------------------------------------------------------------------------------------------------
'''
def Reverse_string(Input_str):
    Reversed_str_list = [list(Input_str)[elements] for elements in range((len(list(Input_str))-1),-1,-1)]
    Reversed_str = "".join(Reversed_str_list)
    return Reversed_str

Output_string = Reverse_string(input("Provide your input string:"))
print(Output_string)
'''
# ----------------------------------------------------------------------------------------------------------
# Program 2.5: Using decorators
# ----------------------------------------------------------------------------------------------------------
'''
def Reverse(Input_str):

    options = print(input("Provide input actions:"
                          "if making mirror image -- enter '1"
                          "making word image --enter '2'"))
    if options == '1':
        def Reverse_string(Input_str):
            Reversed_str_list = [list(Input_str)[elements] for elements in range((len(list(Input_str)) - 1), -1, -1)]
            Reversed_str = "".join(Reversed_str_list)
            print(Reversed_str)
            return Reverse_string

Output_string = Reverse(input("Provide your input string:"))
Output_string()
'''
#=============================================================================================================
# Program 3: Making mirror image of the words"
# input: "Reverse me"
# Output: "me Reverse"
#=============================================================================================================

# ----------------------------------------------------------------------------------------------------------
# Program 3.1: Generic Procedural statements
# ----------------------------------------------------------------------------------------------------------
'''
input_string = "The most effective way to do it is to do it"
str_to_reverse = input_string.split(" ")

Reversed_str = []
for x in range(len(str_to_reverse)-1,-1,-1):
    Reversed_str.append(str_to_reverse[x])
print(" ".join(Reversed_str))
'''
# ----------------------------------------------------------------------------------------------------------
# Program 3.2: Using function and list comprehension
# ----------------------------------------------------------------------------------------------------------
'''
def Reverse_words(Input):
    return (" ".join([Input[x] for x in range(len(Input)-1,-1,-1)]))

Input_list = Reverse_words(input("Provide your String:").split(" "))
print(Input_list)
'''
# ----------------------------------------------------------------------------------------------------------
# Program 3.3: Using List slicing and list comprehension
# ----------------------------------------------------------------------------------------------------------
'''
def Reverse_words(Input):
    return (" ".join(Input[::-1]))

print(Reverse_words(input("Provide your String:").split(" ")))

'''
#=============================================================================================================
# Program 4: Making mirror image of independent - Words position remains same but elements inside each words is reversed"
# input: "Reverse me"
# Output: "esreveR em"
#=============================================================================================================

# ----------------------------------------------------------------------------------------------------------
# Program 4.1: Generic Procedural statements
# ----------------------------------------------------------------------------------------------------------
'''
input_string = "Reverse me"
str_to_reverse = input_string.split(" ")
Reversed_str = []
for x in range(0,len(str_to_reverse)):
    Sub_str = str_to_reverse[x]
    for y in range(len(Sub_str)-1,-1,-1):
        #print(len(str_to_reverse[x])
        Reversed_str.append(Sub_str[y])
    Reversed_str.append(" ")
print("".join(Reversed_str))
'''

# ----------------------------------------------------------------------------------------------------------
# Program 4.2: using function
# ----------------------------------------------------------------------------------------------------------
'''
def Reverse_string(Input_str):
    Input_str_list = Input_str.split(" ")
    Reversed_str_list = []
    for word in Input_str_list:
        for element in range(len(list(word))-1,-1,-1):
            Reversed_str_list.append(word[element])
        Reversed_str_list.append(" ")
    Reversed_str = "".join(Reversed_str_list)
    return Reversed_str

String_to_reversed = Reverse_string(input("Provide your string:"))
print(String_to_reversed)
'''
# ----------------------------------------------------------------------------------------------------------
# Program 4.3: Using string slicing Function and List comprehension
# ----------------------------------------------------------------------------------------------------------
'''
def Reverse_string(Input_str):
    Input_string_list = Input_str.split(" ")
    Reverse_string_list = [x[::-1] for x in Input_string_list]
    return(" ".join(Reverse_string_list))

String_to_reversed = Reverse_string(input("Provide your string:"))
print(String_to_reversed)
'''
#=============================================================================================================
# Program 5: Combination of program 4, program 3 and program 2
# 1. Reversing a string
# 2. Reversing words in a string
# 3. Reversing characters in the words of a string
#=============================================================================================================
'''
def Reverse_function(Input):
    return (Input[::-1])

Input_option = input("Provide action to do:\n"
                     "1 for reversing a string\n"
                     "2 for reversing words in a string\n"
                     "3 for reversing characters in the words of a string\n"
                     "option: ")
if int(Input_option) == 1:
    print(Reverse_function(input("provide your string:")))

elif int(Input_option) == 2:
    print(" ".join(Reverse_function(input("Provide your String:").split(" "))))

elif int(Input_option) == 3:
    print(" ".join(Reverse_function(x) for x in input("Provide your string:").split(" ")))

'''
#=============================================================================================================
# Program 6: Find the duplicate characters in a string
# input: Arpan
# output: "a"
#=============================================================================================================

# ----------------------------------------------------------------------------------------------------------
# Program 6.1: Using general procedural statements and list
# ----------------------------------------------------------------------------------------------------------
'''
input_str = input("provide the string")
Duplicate_char = []
input_str_list = list(input_str)

for x in input_str_list:
    count = 0
    for y in input_str_list:
        if x == y and x not in Duplicate_char:
            count += 1
            if count > 1 and x is not " ":
                Duplicate_char.append(x)

print(Duplicate_char)
'''
# ----------------------------------------------------------------------------------------------------------
# Program 6.2: Using general procedural statements with strings
# ----------------------------------------------------------------------------------------------------------
'''
input_str = input("provide the string").lower()
Duplicate_char = []
#input_str_list = list(input_str)

for x in input_str:
    count = 0
    for y in input_str:
        if x == y and x not in Duplicate_char:
            count += 1
            if count > 1 and x is not " ":
                Duplicate_char.append(x)


print(Duplicate_char)
'''
# ----------------------------------------------------------------------------------------------------------
# Program 6.3: Using Functions and count module of string
# ----------------------------------------------------------------------------------------------------------
'''
def Duplicate_finder(Input_str):
    Duplicate_char = []
    for x in Input_str:
        char_count = Input_str.count(x,0,len(Input_str))
        if char_count > 1 and x is not ' ' and x not in Duplicate_char:
            Duplicate_char.append(x)
    return Duplicate_char
'''
# ----------------------------------------------------------------------------------------------------------
# Program 6.4: Using Functions and count module of string with list comprehension
# ----------------------------------------------------------------------------------------------------------
'''
def Duplicate_finder(Input_str):
    Duplicate_char = [x for x in Input_str if Input_str.count(x) > 1 and x is not ' ']
    return Duplicate_char

Output_char_list = Duplicate_finder(input("provide your string").lower())
print(set(Output_char_list))
'''

# ----------------------------------------------------------------------------------------------------------
# Program 6.5: Using function and dictionary
# ----------------------------------------------------------------------------------------------------------
'''
def Duplicate_finder(Input_str):
    Duplicate_char = {}
    for chr in Input_str:
        if chr in Duplicate_char and chr is not " ":
            Duplicate_char[chr] += 1
        else:
            Duplicate_char[chr] = 1
    return Duplicate_char

count = Duplicate_finder(input("Provide your input string:").lower())
for key in count:
    if count[key] > 1:
        print(key, ":", count[key])
'''
#=============================================================================================================
# Program 7: Find the duplicate words in a string
# input: Arpan is great, arpan is handsome, and arpan is awesome
# output: "arpan","is"
#=============================================================================================================

# ----------------------------------------------------------------------------------------------------------
# Program 7.1: Using general procedural statements
# ----------------------------------------------------------------------------------------------------------
'''
input_str = input("provide the string")
Duplicate_char = []
input_str_list = input_str.split(" ")

for x in input_str_list:
    count = 0
    for y in input_str_list:
        if x is not " " or x is not "\n":
            if y == x and y not in Duplicate_char:
                count += 1
                if count > 1:
                    Duplicate_char.append(y)
            else:
                continue

print(Duplicate_char)
'''
# ----------------------------------------------------------------------------------------------------------
# Program 7.2: Using string count for identifying duplicate characters
# Not a perfect match as count function is used, not to quote
# ----------------------------------------------------------------------------------------------------------
'''
def Repeated_words(Input_string):
    Repeated_words_list = []
    Input_string_list = Input_string.split(" ")
    for x in Input_string_list:
        count = Input_string.count(x)
        if count > 1 and x not in Repeated_words_list:
            Repeated_words_list.append(x)
    return Repeated_words_list

Repeated_words_list = Repeated_words(input("Provide your string:"))
print(Repeated_words_list)
'''
# ----------------------------------------------------------------------------------------------------------
# Program 7.3: Using Function and Dictionaries
# ----------------------------------------------------------------------------------------------------------
'''
def Repeated_words(Input_string):
    Repeated_words_dic = {}
    Input_string_list = Input_string.split(" ")
    for x in Input_string_list:
        if x in Repeated_words_dic:
            Repeated_words_dic[x] += 1
        else:
            Repeated_words_dic[x] = 1
    return Repeated_words_dic

Repeated_words_dic = Repeated_words(input("Provide your string:"))
for key in Repeated_words_dic:
    if Repeated_words_dic[key] > 1:
        print(key, ": ", Repeated_words_dic[key])
'''
#=============================================================================================================
# Program 8: Find the word in pairs which are repeated in a file. Also should remove any special characters in the words.
# input: Arpan Behera, Steve jobs, william shakespear, Arpan Behera, William richardson
# output: Arpan Behera
#=============================================================================================================

# ----------------------------------------------------------------------------------------------------------
# Program 8.1: Using functions and procedural statement
# ----------------------------------------------------------------------------------------------------------
'''
def Words_pair(Input):
    Input_list = Input.split(" ")
    repeated_list = []
    for x in range(0,len(Input_list)-1):
        if x != len(Input_list):
            word_search = ''.join(filter(str.isalnum,str(Input_list[x]))) + " " + ''.join(filter(str.isalnum,str(Input_list[x+1])))
            print(word_search)
            count = Input.count(word_search)
            if count > 1:
                repeated_list.append(word_search)
    return repeated_list


file_input = open("Input_7.txt",'r')
Input = str(file_input.read()).lower()
pair_words = Words_pair(Input)
print(set(pair_words))
'''
#=============================================================================================================
# Program 9: Password check validation
# Check the password matches the criteria for
# 1. Starts with alphabets
# 2. Have atleast 1 uppercase letter
# 3. have atleast 1 special character from the set " !"#$%&'~ "
# 4. have atleast 1 number
# 5. Minimum 8 characters and maximum 15 characters
#=============================================================================================================

# ----------------------------------------------------------------------------------------------------------
# Program 9.1: Using string inbuilt function
# ----------------------------------------------------------------------------------------------------------
'''
def Initial_letter_check(password):
    if password[0:1].isalpha():
        print("1st character Alphabet: passed")
        return True
    else:
        print("1st character should be Alphabet")
        return False

def Uppercase_letter_check(password):
    count = False
    for letter in password:
        if letter.isupper():
            count = True
            break
    if count:
        print("Uppercase character check: passed")
        pass
    else:
        print("Require atleast one Uppercase character")
    return count

def Special_char_check(password):
    allowed_special_char = "!\"#$%&'~"
    for letter in allowed_special_char:
        if letter in password:
            print("Special character check: passed")
            return True
    print("Require atleast 1 special character")
    return False

def Number_check(password):
    for letter in password:
        if letter.isdigit():
            print("Digit check: passed")
            return True
    print("Atleast 1 digit required")
    return False

def letters_count_check(password):
    return 8 <= len(password) <= 15


password = input("Enter Your Password:")
if Initial_letter_check(password) and Uppercase_letter_check(password) and Special_char_check(password) and Number_check(password) and letters_count_check(password):
    print("Password accepted")
else:
    print("password criteria failed")

'''
# ----------------------------------------------------------------------------------------------------------
# Program 9.2: Using converting the values to ascii and verifying criteria
# ----------------------------------------------------------------------------------------------------------
'''
def Initial_letter_check(password):
    Ascii_value = ord(password[0:1])
    if 65 <= Ascii_value <= 90 or 97 <= Ascii_value <= 122:
        print("!st letter alphabet check: passed")
        return True
    else:
        print("1st character require to be alphabet")
        return False

def Uppercase_letter_check(password):
    for letter in password:
        if 65 <= ord(letter) <= 90:
            print("Uppercase character check: passed")
            return True
    print("Require atleast one Uppercase character")
    return False

def Special_char_check(password):
    #allowed_special_char = "!\"#$%&'~"
    for letter in password:
        int_value = ord(letter)
        if 33 <= int_value <=37 or int_value == 64 or int_value == 127:
            print("Special character check: passed")
            return True
    print("Require atleast 1 special character")
    return False

def Number_check(password):
    for letter in password:
        if 48 <= ord(letter) <= 57:
            print("Digit check: passed")
            return True
    print("Atleast 1 digit required")
    return False

def letters_count_check(password):
    return 8 <= len(password) <= 15


password = input("Enter Your Password:")
if Initial_letter_check(password) and Uppercase_letter_check(password) and Special_char_check(password) and Number_check(password) and letters_count_check(password):
    print("Password accepted")
else:
    print("password criteria failed")
'''

# ----------------------------------------------------------------------------------------------------------
# Using Ascii values and optimization
# ----------------------------------------------------------------------------------------------------------
# def character_check(password):
#     letter1_check = True
#     letter_upp_check = 0
#     letter_digit_check = 0
#     letter_special_check = 0
#     if password[0:1].isalpha():
#         print("1st character Alphabet: passed")
#         for letter in password:
#             int_value = ord(letter)
#             if 65 <= int_value <= 90:
#             print("!st letter alphabet check: passed")
#
#         elif 97 <= int_value <= 122:

#=============================================================================================================
# Program 10: Calculate the length of a string without any function
# input: "Arpan"
# output: 5
#=============================================================================================================
'''
def String_length_calculate(Input_str):
    length = 0
    for x in Input_str:
        length += 1
    return length


Input_str = str(input("provide the string:"))
Str_length = String_length_calculate(Input_str)
print(Str_length)
'''
#=============================================================================================================
# Program 11: Count the number if character in a string/file
# input: Google.com
# output: G - 2 , o - 3, l - 1, e - 1, . - 1, c - 1, m - 1
#=============================================================================================================

# ----------------------------------------------------------------------------------------------------------
# Program 11.1: Using string count function and dictionary
# ----------------------------------------------------------------------------------------------------------
'''
def character_count(string_input):
    out = {}
    for char in string_input:
        if char in out and char is not " ":
            out[char] += 1
        elif char is not " ":
            out[char] = 1
    return out

Input_str = input("Provide your input either any file or string:")
if ".txt" in Input_str:
    with open(Input_str,'r') as f:
        string = f.read()
        output = character_count(string.lower())
else:
    output = character_count(Input_str.lower())

print(output)
'''

#=============================================================================================================
# Program 12: Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
#=============================================================================================================
'''

def Fetch_str(Input_str):
    if len(Input_str) < 2:
        out_str = ""
    else:
        out_str = Input_str[:2] + Input_str[-2::1]
    print(out_str)

Fetch_str(input("Provide your string:"))

'''
#=============================================================================================================
# Problem 13: Convert numbers base 8(Oct-decimal), base 16(Hexadecimal), base 2(Binary) to Int base 10(decimal)
# Input:
# Base Factor input >> 8
# Input Number >> 765
# Output: 501
#
# Base Factor input >> 16
# Input Number >> ADF123
# Output: 11399459
#
# Base Factor input >> 2
# Input Number >> 101101
# Output: 45
#
# Any other input gives an error.
# #=============================================================================================================
'''
def base_bin_to_int(Input_number):
    Out_bin_to_int = []
    multiplier = 1
    for x in range(len(Input_number)-1,-1,-1):
        if x == len(Input_number)-1:
            Out_bin_to_int.append(int(Input_number[x]))

        else:
            multiplier *= 2
            Out_bin_to_int.append(int(Input_number[x]) * multiplier)
    print(sum(Out_bin_to_int))

def base_oct_to_int(Input_number):
    Out_oct_to_int = []
    multiplier = 1
    for x in range(len(Input_number)-1,-1,-1):
        if x == len(Input_number)-1:
            Out_oct_to_int.append(int(Input_number[x]))

        else:
            multiplier *= 8
            Out_oct_to_int.append(int(Input_number[x]) * multiplier)
    print(sum(Out_oct_to_int))


def base_hex_to_int(Input_number):
    Out_hex_to_int = []
    base_dict = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    multiplier = 1
    for x in range(len(Input_number)-1,-1,-1):
        if x == len(Input_number)-1:
            if Input_number[x] in base_dict:
                Out_hex_to_int.append(base_dict[Input_number[x]])
            else:
                Out_hex_to_int.append(int(Input_number[x]))
        else:
            multiplier *= 16
            if Input_number[x] in base_dict:
                Out_hex_to_int.append(base_dict[Input_number[x]]*multiplier)
            else:
                Out_hex_to_int.append(int(Input_number[x])*multiplier)
    print(sum(Out_hex_to_int))

def base_int_to_hex(Input_number):
    Out_int_to_hex = []
    base_dict = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    divisor = 16
    Input_number_temp = Input_number
    while int(Input_number_temp)/divisor == 0:
        Input_number_temp = Input_number_temp/divisor
        remainder = Input_number_temp%divisor
        if remainder < 10:
            Out_int_to_hex.append(remainder)
        else:
            Out_int_to_hex.append(base_dict[remainder])
    print(reversed(Out_int_to_hex))


Base_factor = int(input("Any base to int input"
                        "'8' : oct to int"
                        "'16' : hex to int"
                        "'2' : bin to int"
                        "Base Factor input >>"))

Input_number = input("Input Number >> ")
if Base_factor == 8:
    Oct_data = ["0","1","2","3","4","5","6","7"]
    for x in Input_number:
        if x not in Oct_data:
            print("Oct number is 0-7, kindly provide input inbetween")
            exit()
    base_oct_to_int(Input_number)

elif Base_factor == 16:
    Hex_data = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    for x in Input_number:
        if x not in Hex_data:
            print("Hex number is 0-9 & A-F, kindly provide inbetween")
            exit()
    base_hex_to_int(Input_number)

elif Base_factor == 2:
    Bin_data = ["0","1"]
    for x in Input_number:
        if x not in Bin_data:
            print("Bin number contains only 0 and 1, kindly provide inbetween")
            exit()
    base_bin_to_int(Input_number)

else:
    print("Input doesn't match any")
'''

