# from unittest import result
# import random_coder
# from decimal import ROUND_UP


15# the_num = len('abcdefghijklmnopqrstuvwxyz')
# print(the_num)
# my_test_num = str(the_num)
# print("The alphabet has "+my_test_num+" of character in it!")
# a = (123)
# # print(type(a))



# num = "89"
# print(type(num))



# the_spliter1 = int(num[0]) 
# print(type(the_spliter1))


# the_spliter2 = int(num[1]) 
# print(type(the_spliter2))

# the_mixologist = the_spliter1 + the_spliter2


# print(the_mixologist)

# height = input("Enter your Height please")
# weight = input("Enter your Weight please")

# num1= float(height)
# num2 = int(weight)

# cal_bmi = num2 / num1 ** 2 

# print(cal_bmi)

# print(type(num1))
# print(type(num2))
# print(type(cal_bmi))



# print(round(8/3) )


# score = 0 
# height = 1.8
# isWinning = True

# #f-sting

# print(f"your score is  {score}, your height is {height}, and it is {isWinning} that your are winning")



 
# age =input("What is your current age")


# # users age
# days_lived = 365 * int(age)
# weeks_lived = 52 * int(age)
# months_lived = 12 * int(age)

# # What user has left

# days_left = 365 * 90
# weeks_left = 52 * 90
# months_left = 12 * 90

# days = days_left - days_lived
# weeks = weeks_left - weeks_lived
# months = months_left - months_lived






# print(f"You have {days} days , {weeks} weeks ,and {months} months left to live")




# bill_total = float(input("What was the total bill?"))
# tip =  int(input("What percentage tip would you like to give? 10, 12, or 15?"))
# how_split = int(input("How many people are spliting the bill"))

# tip_section = int(tip / 100 * bill_total)
# per_person = int(how_split * bill_total)
# plus_tip = per_person + tip_section


# print(tip_section)
# print()
# print(how_split)
# print(f"You tip total with you percent at {tip}% is equal to {tip_section}. So each person will pay {plus_tip}$ each ")




# print(type(bill_total))
# print(type(tip))
# print(type(how_split))
# print(type(how_split))
# print(tip_section)

# print(type(percentage))
# print(round(percentage))







# number = int(input("What is the number"))

# if number % 2 == 0 :
#     print("its an even number right!")
#     sec_guess = str(input("is it less than 14 ?"))
#     if sec_guess.upper == "yes" :
#         print("is it 12" )
#     else: print("is it 18")

# elif number % 2 != 0 :
#     print("its an odd number right!")
#     sec_guess = str(input("is it less than 15 ?"))
#     if sec_guess.upper == "yes":
#         print("is it 13" )
#     else: print("is it 19")

# else:
#     print("Ill get it next time!")



# Water boil

# boiling = input("What is the temp of your water?")

# if int(boiling) <= 211 :
#     print(f"{boiling} degrees is not hot enough")

# elif int(boiling) == 212 :
#     print(f"{boiling} degrees is the perfect temp")

# elif int(boiling) >= 213 :
#     print(f"{boiling} degrees is beyond the boiling point")


# year = input("What year ?")

# if int(year) % 4 == 0 :
#     if int(year) % 100 != 0 :
#         if int(year) % 400 == 0 :
#             print(f"{year} is  a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else :
#         print(f"{year} is not a leap year")
# else :
#         print(f"{year} is not a leap year")


# # Pizza Size
# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25

# # Toppings
# pepperoni_for_small = 2
# pepperoni_for_medium = 3
# pepperoni_for_large = 4
# extra_cheese = 1


# choose_pizza_size = input(str("what size pizza would you like ? S, M, L")).upper()
# print(choose_pizza_size)
# if choose_pizza_size == "S" :
#     print(small_pizza)
#     choose_topping = input(str("Would you like extra topping , like pepperoni or cheese")).upper()
#     if choose_topping == "CHEESE" :
#         print(f"your total for the small pizza and extra cheese is {int(small_pizza + extra_cheese)}")
    
#     elif choose_topping == "PEPPERONI" :
#         print(f"your total for the small pizza and extra pepperoni is {int(small_pizza + pepperoni_for_small)}")

#     elif choose_topping == "PEPPERONI & CHEESE":
#         print(f"your total for the small pizza and extra pepperoni and extra cheese is {int(small_pizza + pepperoni_for_small + extra_cheese)}")





# elif choose_pizza_size == "M" :
#     print(medium_pizza)
#     choose_topping = input(str("Would you like extra topping , like peperoni or cheese")).upper()
#     if choose_topping == "CHEESE" :
#         print(f"your total for the medium pizza and extra cheese is {int(medium_pizza + extra_cheese)}")

#     elif choose_topping == "PEPPERONI" :
#         print(f"your total for the medium pizza and extra pepperoni  is {int(medium_pizza + pepperoni_for_medium)}")

#     elif choose_topping == "PEPPERONI & CHEESE":
#         print(f"your total for the medium pizza and extra pepperoni and extra cheese  is {int(medium_pizza + pepperoni_for_medium + extra_cheese)}")





# elif choose_pizza_size ==  "L" :
#     print(large_pizza)
#     choose_topping = input(str("Would you like extra topping , like peperoni or cheese")).upper()
#     if choose_topping == "CHEESE" :
#         print(f"your total for the large pizza and extra cheese is {int(large_pizza + extra_cheese)}")

#     elif choose_topping == "PEPPERONI" :
#         print(f"your total for the large pizza and extra pepperoni  is {int(large_pizza + pepperoni_for_large)}")

#     elif choose_topping == "PEPPERONI & CHEESE":
#         print(f"your total for the large pizza and extra pepperoni  and extra cheese is {int(large_pizza + pepperoni_for_large + extra_cheese)}")

# else: print("Please choose a size!")

# light= 1
# fast_pased = 2
# moderate = 3 
# hard = 4
# gunns_blazing = 5

# name = input("name")
# diff = input("on a scale of one to 5 how dificutly was your workout")

# if diff == "1" :
#     print("light")
# elif diff == "2" :
#     print("fast_pased")
# elif diff == "3" :
#     print("moderate")
# elif diff == "4" :
#     print("hard")
# elif diff == "5" :
#     print("gunns_blazing")




# print(f"Great work today {name}, Consistancy is the goal so keep it up and shoot higher than {diff}")







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

# How to plug in random numbers from another file example!!!
# print(random_coder.results)

row1 = ["🙂.1","🙂.2","🙂.3"]
row2 = ["🙂1.1","🙂1.2","🙂1.3"]
row3 = ["🙂2.1","🙂2.2","🙂2.3"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?")
one = int(position[0])
two = int(position[1])

results = map[one - 1]
results[two - 1] = "X"
# first_row0 = results[0]




# print(results)
# print(results[1])
# print(results2)

print(results)