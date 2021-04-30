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
        print(f'\nOrder Ticket #{receipt}')

        entree, e_price = getEntree()
        side, s_price = getSide()

        print(f'\n{entree}\t\tPrice: ${e_price:.2f}')
        print(f'{side}\t\tPrice: ${s_price:.2f}')

        orders += -1
    

## Entree function: getEntree()
def getEntree():
    entree = int(input('\nEnter\t[1] for a Hamburger\n\t[2] for a Cheeseburger\n\t[3] for a Chicken Sandwich,\n\t[4] for no sandwich..\n\nYour Selection: '))
    entree_price = 0.00

    if entree == 1:
        sammich = 'Hamburger'
        entree_price = hamburger
    elif entree == 2:
        sammich = 'Cheeseburger'
        entree_price = cheeseburger
    elif entree == 3:
        sammich = 'Chkn-Sandwich'
        entree_price = sandwich
    elif entree == 4:
        sammich = 'No Sammich'
    else:
        print('Invalid, try again!')
        getEntree()
        
    return sammich, entree_price

## Side-Order function: getSide()
def getSide():
    side = int(input('\nEnter\t[1] for a French Fries,\n\t[2] for Onion Rings,\n\t[3] for a Side Salad,\n\t[4] for NO side..\n\nYour Selection: '))
    side_price = 0.00

    if side == 1:
        side = 'French Fries'
        side_price = fries
    elif side == 2:
        side = 'Onion Rings'
        side_price = rings
    elif side == 3:
        side = 'Side Salad'
        side_price = salad
    elif side == 4:
        side = 'No Side'
    else:
        print('Invalid, try again!')
        getSide()

    return side, side_price

## Drink function: getDrank()


main()