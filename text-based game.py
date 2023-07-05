import random
# # Treasure island
# print('''*******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************
# ''')

# name = input("What is your Name?")
# print (f"Welcome {name} to Treasure Island.")
# first_Q = input(f"{name} which way do you want to start this journey , straight right or left").lower()


# if first_Q == "straight" :
#     second_q =input(str("Right choice, now you see a bridge choose straight or right or left")).lower()
#     if second_q == "left" :
#         print(f"{name} you made it to the treasure")

#     else: (f"{name} you died from babboons . Game Over")







# elif first_Q == "right" :
#   second_q =input(str("Right choice, now you see a somthing that was recently buried, do you wanna investagate yes or no ")).lower()
#   if second_q == "yes" :
#     print(f"{name} you died, it was a claymore!! ")

#   elif second_q == "no": (f"{name} you now see a lake the left side is blocked off so you can swim accross or walk around the right side , which one swim of right")
  
#   third_Q = input(f"{name} which way do you want to start this journey , straight right or left").lower()
#   if third_Q == "swim" :
#     print(f"{name} you were eaten. Game Over")
#   elif third_Q == "right" :
#    print(f"{name} you made it to the treasure")



# elif first_Q == "left" :
#    print(f"{name} you were eaten. Game Over")





# Useing the max method you can sort to the highest of each data type, exceppted booleans. 
# class_scores = [98,110,15,1,34,26,33,346,0.1,56,3445,91,234,60,553]# it even sorts floats / deciamals
# array2 = [1, 2, 3, 4, 5]
# array3 = ['apple', 'banana', 'cherry', 'date','zack','paul']
# array5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# array6 = list(range(1, 1001))

# print(len(class_scores))
# class_scores.sort()
# print(class_scores)

# print(len(class_scores))
# print(class_scores[13])
# print(max(class_scores))
# print(max(array2))
# print(max(array3))
# print(max(array5))
# print(max(array6))

# Useing the min method you can sort to the lowest of each data type, exceppted booleans. 
# print(min(class_scores))
# print(min(array2))
# print(min(array3))
# print(min(array5))
# print(min(array6))

# for number in range(0, 1100, 100):
#     print(number)


# total = 0 
# for number in range(2, 101, 2):
#     total += number
#     print(total)


# divided by 3 = fizz

# divided by 5 = buzz

# divided by 3 and 5 = fizz buzz


# for number in range(1, 101):
#     if number % 3 == 0  and number % 5 == 0 :
#         print("Fizz Buzz")
#     elif number % 3 == 0 :
#         print("fizz")
#     elif number % 5 == 0 :
#         print("buzz")
#     else: 
#         print(number)



# print("Welcome to the Password generator")
# nr_count = int(input("How many Characters would you like your password to be ? 8 , 10 or 12"))

# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# number = ['0','1','2','3','4','5','6','7','8','9']
# symbols = ['!', '#', '$','%','&','(',')','*','+']

# random_alp1 = random.choice(alphabet)
# random_number1 = random.choice(number)
# random_symbol1 = random.choice(symbols)
# random_alp2 = random.choice(alphabet)
# random_number2 = random.choice(number)
# random_symbol2 = random.choice(symbols)
# random_alp3 = random.choice(alphabet)
# random_number3 = random.choice(number)
# random_symbol3 = random.choice(symbols)
# random_alp4 = random.choice(alphabet)
# random_number4 = random.choice(number)
# random_symbol4 = random.choice(symbols)





# eight = (f"{random_alp1}{random_number1}{random_symbol1}{random_alp2}{random_number2}{random_symbol2}{random_alp3}{random_number3}")

# ten = (f"{random_alp1}{random_number1}{random_symbol1}{random_alp2}{random_number2}{random_symbol2}{random_alp3}{random_number3}{random_symbol3}{random_alp4}")

# twelve = (f"{random_alp1}{random_number1}{random_symbol1}{random_alp2}{random_number2}{random_symbol2}{random_alp3}{random_number3}{random_symbol3}{random_alp4}{random_number4}{random_symbol4}")

# # print(eight)
# # print(ten)
# # print(twelve)
# # make the first question ask it the user wants 8 , 10, or 12 char in the passwords
# if nr_count == 8:
#     print(eight)
# elif nr_count == 10:
#     print(ten)
# elif nr_count == 12:
#     print(twelve)