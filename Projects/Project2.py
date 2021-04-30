##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Project 2
# Due Date: 05.  .21
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

# subTotal + Tax:
subtotal = 0.00
TAX = 0.08

print('\n*** *** *** *** *** Welcome *** *** *** *** ***')
print('\n**** *** *** Binary Burger Program *** *** ****\n')

print("\t\t 5112 E. MLK BLVD")
print("\t\tLONG BEACH, CA 90806 ")
print("\t\t    503.323.2342\n")
print("Server: Kim Davis \t\t\t03/21/21")
print("Guests: 1\t\t\t\t11:11 AM")

def main():
    orders = int(input('\nEnter # of Orders: '))
    receipt = 0

    while orders > 0:
        receipt += 1
        print(f'Enter Order #{receipt}')

        entree = getEntree()
        print(f'Price of Entree: {entree}')

        orders += -1
    

## def for getEntree()
def getEntree():
    entree = int(input('\nEnter\t[1] for a Hamburger\n\t[2] for a Cheeseburger\n\t[3] for a Chicken Sandwich,\n\t[4] for no sandwich..\n\nYour Selection: '))
    
    if entree == 1:
        entree_price = hamburger
        print(f'Hamburger\t\t${hamburger:.2f}')
        return entree_price
    elif entree == 2:
        entree_price = cheeseburger
        print(f'Cheeseburger\t\t${cheeseburger:.2f}')
        return entree_price
    elif entree == 3:
        entree_price = sandwich
        print(f'Chicken Sandwich\t${sandwich:.2f}')
        return entree_price
    elif entree == 4:
        entree_price = 0
        print('No Entree')
        return entree_price
    else:
        print('Invalid Entry')
        getEntree()

    

## def for getSide()

## def for getDrank()

main()