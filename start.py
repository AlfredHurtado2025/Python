# ---------------------------------Print Functions------------------------------------

print("I am Iron Man\nNo, I am Tony Stark\nNo, I am Poppy")

print("""
I am iron Man.
No, I am Tony Stark.
No, I am Poppy.
      """)

print("I am Iron Man. \n" + "No, I am Tony Stark.\n" + "No, I am Poppy.")
print()
print("Hello\n" * 3)

# --------------------------------------MATH------------------------------------------

name = "Alfred"

age = 19
act_age = 19.95
math = 5 * 5 ** 3 + 5 / 2 - 3

results = age + act_age + math
print(results)

print(name)
print(age)

print(type(name))
print(type(age))
print(type(act_age))

# ------------------------------"if" statements---------------------------------------

name = input("What is your name:\n")
if name != "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
         print("Get out Ben.")
         exit()
    else:
        print("Welcome in Ben!!!")
else:
     print(f"Hello {name}, Welcome to NetworkChuck Coffee!!!!")


# -----------------------------"elif" statement---------------------------------------
order = "Black Coffer.\n Latte"

if order == "Black Coffee":
    price = 13 
elif order == "Latte":
   price = 5

# -------------------------------List Statement---------------------------------------

camping_stuff = ["Tent", "Sleeping bags", "Knife", "Raspberry pi", "Coffee", 
              "Ethernet cable", "Flash drive", "Marshmellow "]

camp_site = ["Crystal Lake", 404, 89.3, True]

# Add stuff to the end of list.
camping_stuff.append("Toilet paper")
camping_stuff.append("Bidet")

# Add Multiple things at the end of list at once.
camping_stuff.extend(["Toilet paper", "bidet"])
camping_stuff = camping_stuff + ["Toilet paper", "bidet"]

# Add stuff at the start of list.
camping_stuff.insert(0, "Bidet")
camping_stuff.insert(-1, "Toilet paper")

# Remove stuff from list
camping_stuff.clear()
camping_stuff.remove("Tent")
camping_stuff.remove("Sleeping bags")
print(f"This Item was just deleted from your bag:", {camping_stuff.pop(0)})
camping_stuff.pop(0)

me = camping_stuff[4]
you = camping_stuff[-2]
print(me)
print(you)
print(camping_stuff)

# ---------------------------------Tuples statement----------------------------------

AlfredHurtado = ("Alfred", 20, "Car guy")
print(type(AlfredHurtado))
(name, age, person) = AlfredHurtado
print(name)
print(age)
print(person)

atuple = 1, 
print(type(atuple))

#----------------------------------Coffee Shop Lab------------------------------------

# Welcome Banner

name = input("What is your name:\n")
print()
if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil?\n")
    deeds = int(input("How many good Deeds have you done today:\n "))
    if evil_status == "Yes" and deeds < 4:
        print(f"GET OUT OF HERE EVIL {name}!!!")
        exit()
    else:
        print("Welcome in Ben!!!")
else:
    print(f"Hello {name}, Welcome to NetworkChuck Coffee!!!!")
    print()

# # Menu Bar
print("----------------------MENU---------------------")
menu = "Black Coffee: $3.00 \nEspresso: $5.00 \nLatte: $9.00 \nCappucino: $10.00\nFrappuccino: $13.00"
print(f"{name}, what would you like from our Menu today? \nHere is what we are serving:\n{menu}")
print()

# # Customer Order
order = input()

if order == "Frappuccino":
    price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    toppings = "Yes"
    answer = "No"
    if toppings == "Yes":
        input("Would you like whipped cream: ")
        if answer == "No":
            exit()
        print("Adding whipped cream!!")
        price = 11
    else:
        price = 9
        exit()
elif order == "Cappucino":
    price = 10
else:
    print("Sorry, we don't have that here.")
    exit()
print()

quantity = input(f"How many {order} would you like:\n")
total = price * int(quantity)

print(f"Sounds good {name}, we'll have your {quantity} {order}'s coming right up!!!")
print()
print(f'Thank you, your total is: ${total}!!!')




