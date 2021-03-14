##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Project 1
# Due Date: 03.21.21
# ####################################################

## Binary Burgers ##

# Burger + Sandwich prices:
hamburger = 2.75        # option [1]
cheeseburger = 3.25     # option [2]
sandwich = 2.50         # option [3]

# Side-Order prices:
fries = 2.25            # option [1]
rings = 1.75            # option [2]
salad = 1.50            # option [3]

# Drink prices:
sm = 1.50               # option [1]
med = 2.25              # option [2]
lg = 2.75               # option [3]
h2o = 0.00              # option [4]

print('\n*** *** *** *** Binary Burger Program *** *** *** ***\n')

meal = int(input('Enter\t[1] for a Hamburger\n\t[2] for a Cheeseburger\n\t[3] for a Chicken Sandwich,\n\t[4] for no sandwich..\n\nYour Selection: '))
side = int(input('Enter\t[1] for a French Fries,\n\t[2] for Onion Rings,\n\t[3] for a Side Salad,\n\t[4] for NO side..\n\nYour Selection: '))
drink = int(input('Enter\t[1] for Coke\n\t[2] for Sprite\n\t[3] for Lemonade\n\t[4] for Water\n\nYour Selection: '))
size = int(input('Enter\t[1] for Small,\n\t[2] for Medium,\n\t[3] for Large\n\nYour Selection: '))

if meal < 1 or meal > 4:
    meal = 4
elif meal == 1:



print('Here is your order: \n')