import random

paper = 1
rock = 2
scissors = 3 
choices = [rock ,scissors ,paper ]
computer_choice = [paper, rock, scissors]

user_choose = int(input("you versus the computer? choose 0 for rock,  1 for scissor or 2 for paper. "))

#users
user_choice = choices[user_choose]

# computer_generatered
length = len(computer_choice) - 1
random_int = random.randint(0, length)
computer_choose = computer_choice[random_int]


print(user_choice)
print(computer_choose)




#comp win
if user_choice == paper and computer_choose == rock:
   print ("user won")


elif user_choice == scissors and computer_choose == paper:
   print ("user won")

elif user_choice == rock and computer_choose == scissors:
    print("user won")

#user win

elif user_choice == rock and computer_choose == paper:
   print ("computer won")

elif user_choice == paper and computer_choose == scissors:
   print ("computer won")

elif user_choice == scissors and computer_choose == rock:
    print("computer won")

#ties

elif user_choice == scissors and computer_choose == scissors:
    print("it's a tie")

elif user_choice == rock and computer_choose == rock:
    print("it's a tie")

elif user_choice == paper and computer_choose == paper:
    print("it's a tie")