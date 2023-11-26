# # Loops
# # example 1
# fruits = ["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)

# # example 2
# students_heights = input().split()
# for n in range(0, len(students_heights)):
#     students_heights[n] = int(students_heights[n])
# total_height = 0
# for height in students_heights:
#     total_height += height
# print(f"total height = {total_height}")
# number_of_students = 0
# for students in students_heights:
#     number_of_students += 1
# print(f"Number of students {number_of_students}")

# average_height = round(total_height/number_of_students)
# print(f"average height = {average_height}")

# # example 3
# student_scores = input().split()
# for n in range(0,len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"Score = {highest_score}")

# # for loop with range
# for number in range(1,10):
#     print(number)

# # example 4
# total = 0
# for number in range(1,101):
#     total += number
# print(total)

# # fizz buzz
# target = 100
# for number in  range(1, target + 1):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
        
# password generator
import random
letters = ['q','w','e','r','t','y','u','i','o','p',
           'a','s','d','f','g','h','j','k','l',
           'z','x','c','v','b','n','m',
           'Q','W','E','R','T','Y','U','I','O','P',
           'A','S','D','F','G','H','J','K','L',
           'Z','X','C','V','B','N','M']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','&','*']
print("Welcom to Password Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
# # Easy
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1,nr_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)
# Hard
password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1,nr_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your pass word is {password}")