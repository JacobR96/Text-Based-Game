import random


# randum_int = random.randint(1, 10)
# randum_int2 = random.randint(1, 10)
# results = randum_int * randum_int2
# # print(randum_int * randum_int2)



# # random_float = random.random()
# # print(random_float)

# head_tails = random.randint(1, 2)

# if head_tails == 1 :
#     print("Heads")
# elif head_tails == 2 :
#     print("Tails")


#List or an array in javascript

states = [
    {"Alabama",},
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri"
]
# print(states[1])
# print(states[6])
# print(states[3])
# print(states[16])

# print(states[-16])


#Pushes data to the end of list. more like .push in javascript
# states.append("Jacobsville")
# print(states)


names =  [
    "Emma", "Noah", "Ava", "Liam", "Isabella", "Sophia", "Mason", "Mia", "Benjamin", "Charlotte",
    "Ethan", "Amelia", "James", "Harper", "Elijah", "Evelyn", "Oliver", "Abigail", "William", "Emily",
    "Samuel", "Elizabeth", "Henry", "Sofia", "Alexander", "Avery", "Michael", "Ella", "Jackson", "Scarlett",
    "Sebastian", "Grace", "Aiden", "Chloe", "Matthew", "Victoria", "Joseph", "Riley", "Daniel", "Aria",
    "Carter", "Lily", "David", "Aubrey", "Wyatt", "Zoey", "John", "Penelope", "Owen", "Lillian",
    "Jack", "Addison", "Luke", "Layla", "Gabriel", "Natalie", "Anthony", "Hannah", "Isaac", "Brooklyn",
    "Dylan", "Zoe", "Andrew", "Nora", "Lincoln", "Leah", "Christopher", "Savannah", "Joshua", "Audrey",
    "Grayson", "Claire", "Christian", "Eleanor", "Mateo", "Skylar", "Ryan", "Ellie", "Jaxon", "Samantha",
    "Nathan", "Stella", "Muhammad", "Paisley", "Aaron", "Violet", "Isaiah", "Mila", "Thomas", "Allison",
    "Charles", "Alexa", "Caleb", "Anna", "Josiah", "Hazel", "Hudson", "Aaliyah", "Henry", "Ariana",
    "Eli", "Lucy", "Levi", "Caroline", "David", "Sarah", "Joseph", "Genesis", "Samuel", "Kennedy",
    "Sebastian", "Sadie", "Daniel", "Ruby", "Owen", "Autumn", "Gabriel", "Madeline", "Matthew", "Willow",
    "Connor", "Piper", "Jayden", "Alyssa", "Luke", "Maya", "Isaac", "Nevaeh", "Cameron", "Serenity",
    "Miles", "Eva", "Nicholas", "Adeline", "Leo", "Hailey", "Lincoln", "Kaylee", "Jeremiah", "Natalia",
    "Eli", "Maria", "Josiah", "Eliana", "Colton", "Brian"]

length = len(names) - 1

randum_int = random.randint(0, length)
randum_int2 = random.randint(0, length)
choice = names[randum_int]
choice2 = names[randum_int2]
print(f"{choice} pays the bill and  {choice2} pays a 15% tip ")

print(length)
