# # Data types
# # string
# print("Hello"[0]) # print letter H
# print("Hello"[4]) # print letter o
# "123": with 123 inside "", it become a letter not a number. So if you write: print("123"+"456"), it will not = 579, it will be "123456"

# # Interger
# If you want caculate "123" + "456", you just write 
# print(123 + 456)

# # Float
# sample = 3.14

# # Boolean
# True
# False

# # exampale
# city = "New York"
# print(city[2] + city[5])
# in this code, computer will count the string. Start with N = 0, e = 1 and continue unitl k = 7. When you print city[2] + city[7], computer will get letter "w" and "o" and give answer = "wo"

# # extra example :))
# num_char = len(input("What is your name?\n")) # "\n" is down the line, !important: the output type is "int" so you should convert to string
# new_num_char = str(num_char) # convert step
# print("Your name has " + new_num_char + " characters.")
# print(type(new_num_char)) # check type of new_num_char


# # If you want to know more about type, you can try this example. But you should try one by one.
# num = str(123)
# num = float(123)
# num = int(123)
# print(type(num))

# # plus two digit number
# two_num = input()
# digit_1 = int(two_num(0))
# digit_2 = int(two_num(1))
# two_digit_num = digit_1 + digit_2
# print(two_digit_num)

# BMI caculate
# weight = input("Enter your weight:\n")
# height = input("Enter your height:\n")
# # convert type 
# weight_int = int(weight) # don't need high precision
# height_int = float(height) # need high precision
# # using the exponent operator 2
# bmi = weight_int / height_int ** 2
# # conver type
# bmi_int = int(bmi)
# print(bmi_int)