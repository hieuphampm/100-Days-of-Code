# Randomisation and Python lists
# Random

# # Example 1
# import random as rd
# random_interger = rd.randint(1,10)
# print(random_interger)

# # Example 2
# import random
# random_side = random.randint(0,1)
# if random_side == 1:
#     print("True")
# else:
#     print("False")

# List
# # Example 1
# city_in_VN = ["HoChiMinh","Hanoi","Hue","Danang"]
# print(city_in_VN[2]) # print city at position 2 in list. starting from 0 and ending at 3

# # Example 2
# city_in_VN = ["HoChiMinh","Hanoi","Hue","Danang"]
# city_in_VN[2] = "Quangngai" #Change Hue to Quangngai
# print(city_in_VN)

# # Example 3
# city_in_VN = ["HoChiMinh","Hanoi","Hue","Danang"]
# city_in_VN.extend(["Camau","Hoabinh"]) # add 2 items into list
# print(city_in_VN)

# # Example 4
import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
items = [rock, paper, scissors]
user_choice = int(input("What do you choose? Rock = 0, Paper = 1, Scissors = 2.\n"))
print("You choose")
print(items[user_choice])
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(items[computer_choice])
if user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("Computer win")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice == user_choice:
    print("It's a draw")
elif user_choice >= 3 or user_choice < 0:
    print("You type invalid number, you lose")