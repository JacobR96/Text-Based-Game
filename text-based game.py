
# Treasure island
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

name = input("What is your Name?")
print (f"Welcome {name} to Treasure Island.")
first_Q = input(f"{name} which way do you want to start this journey , straight right or left").lower()


if first_Q == "straight" :
    second_q =input(str("Right choice, now you see a bridge choose straight or right or left")).lower()
    if second_q == "left" :
        print(f"{name} you made it to the treasure")

    else: (f"{name} you died from babboons . Game Over")







elif first_Q == "right" :
  second_q =input(str("Right choice, now you see a somthing that was recently buried, do you wanna investagate yes or no ")).lower()
  if second_q == "yes" :
    print(f"{name} you died, it was a claymore!! ")

  elif second_q == "no": (f"{name} you now see a lake the left side is blocked off so you can swim accross or walk around the right side , which one swim of right")
  
  third_Q = input(f"{name} which way do you want to start this journey , straight right or left").lower()
  if third_Q == "swim" :
    print(f"{name} you were eaten. Game Over")
  elif third_Q == "right" :
   print(f"{name} you made it to the treasure")



elif first_Q == "left" :
   print(f"{name} you were eaten. Game Over")

