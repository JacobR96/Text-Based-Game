
def generate_car_image():
    car_image = r'''
           _______
  _||____||___\_____
 (   '#cars' ____  #\
  '._____.'`______,'_)

'''
    print(car_image)





name = str(input("What is your name?"))
print(f"Hello {name}")
location = str(input("Where to ? Gym Or Commissary"))
if location == str("gym") :
    print("Lets go to the gym! ")

if location == str("commissary"):
    print("Lets go to the Commissary 🥦 ")

print(f"Brr brr Im in me moms car {generate_car_image()}")

