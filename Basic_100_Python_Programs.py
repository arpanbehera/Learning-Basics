print("hello arpan")

#--------------------------------------
#Question 1: Find numbers divisible by 1 number and not divisible by another with output string comma separated
output = []
#output = " "
for number in range(2000,3201):
    if number % 7 == 0 and number % 5 != 0:
        #output = str(number) + "," + output
        output.append(str(number))

print(",".join(output))

# This is a new program that will have some basic usecase