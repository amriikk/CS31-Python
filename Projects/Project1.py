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

# Total + Tax variables:
subtotal = 0.00
TAX = 0.08

print('\n*** *** *** *** *** Welcome *** *** *** *** ***')
print('\n**** *** *** Binary Burger Program *** *** ****\n')

print("\t\t 5112 E. MLK BLVD")
print("\t\tLONG BEACH, CA 90806 ")
print("\t\t    503.323.2342\n")
print("Server: Kim Davis \t\t\t03/21/21")
print("Guests: 1\t\t\t\t11:11 AM")

meal = int(input('\nEnter\t[1] for a Hamburger\n\t[2] for a Cheeseburger\n\t[3] for a Chicken Sandwich,\n\t[4] for no sandwich..\n\nYour Selection: '))
side = int(input('\nEnter\t[1] for a French Fries,\n\t[2] for Onion Rings,\n\t[3] for a Side Salad,\n\t[4] for NO side..\n\nYour Selection: '))
drink = int(input('\nEnter\t[1] for Coke\n\t[2] for Sprite\n\t[3] for Lemonade\n\t[4] for Water\n\nYour Selection: '))
size = int(input('\nEnter\t[1] for Small,\n\t[2] for Medium,\n\t[3] for Large\n\nYour Selection: '))

print('\nHere is your order: \n')


## Meal
if meal < 1 or meal > 4:
    meal = 4
    meal_price = 0.00
    # print(f'No Burger/Sandwich!\t${meal_price:.2f}')
elif meal == 1:
    meal_price = hamburger
    print(f'Hamburger\t\t${hamburger:.2f}')
elif meal == 2:
    meal_price = cheeseburger
    print(f'Cheeseburger\t\t${cheeseburger:.2f}')
elif meal == 3:
    meal_price = sandwich
    print(f'Chicken Sandwich\t${sandwich:.2f}')
else:
    meal_price = 0.00
    # print(f'No Burger or Sandwich selected!')

## Side Order
if side < 1 or side > 4:
    side = 4
elif side == 1:
    side_price = fries
    print(f'French Fries\t\t${fries:.2f}')
elif side == 2:
    side_price = rings
    print(f'Onion Rings\t\t${rings:.2f}')
elif side == 3:
    side_price = salad
    print(f'Side Salad\t\t${salad:.2f}')
else:
    side_price = 0.00
    # print(f'No side order selected!')

## Drink Order
if drink < 1 or drink > 4:
    drink = 'Water'
    drink_size = 'Medium'
    drink_price = h2o

    print(f'{drink_size} {drink}\t{drink_price}')
elif drink == 1: # Coke Selected
    drink = 'Coke'
    if size == 1:
        drink_size = 'Small'
        drink_price = 1.50
    elif size == 2:
        drink_size = 'Medium'
        drink_price = 2.25
    elif size == 3:
        drink_size = 'Large'
        drink_price = 2.75
    else:
        drink_size = 'Medium'
        drink_price = 2.25
    print(f'{drink_size} {drink}\t\t${drink_price:.2f}')
elif drink == 2: # Sprite Selected
    drink = 'Sprite'
    if size == 1:
        drink_size = 'Small'
        drink_price = 1.50
    elif size == 2:
        drink_size = 'Medium'
        drink_price = 2.25
    elif size == 3:
        drink_size = 'Large'
        drink_price = 2.75
    else:
        drink_size = 'Medium'
        drink_price = 2.25
    print(f'{drink_size} {drink}\t\t${drink_price:.2f}')
elif drink == 3: # Lemonade Selected
    drink = 'Lemonade'
    if size == 1:
        drink_size = 'Small'
        drink_price = 1.50
    elif size == 2:
        drink_size = 'Medium'
        drink_price = 2.25
    elif size == 3:
        drink_size = 'Large'
        drink_price = 2.75
    else:
        drink_size = 'Medium'
        drink_price = 2.25
    print(f'{drink_size} {drink}\t\t${drink_price:.2f}')
else: # Water Selected
    drink = 'Water'
    drink_price = h2o
    if size == 1:
        drink_size = 'Small'
    elif size == 2:
        drink_size = 'Medium'
    elif size == 3:
        drink_size = 'Large'
    else:
        drink_size = 'Medium'
    print(f'{drink_size} {drink}\t\t${drink_price:.2f}')

print('-----------------------------')
subtotal = meal_price + side_price + drink_price
tax = subtotal * TAX
total = subtotal + tax
print(f'Subtotal:\t\t${subtotal:.2f} \nTax:\t\t\t${tax:.2f}\nTotal:\t\t\t${total:.2f}\n')