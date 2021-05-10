##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Project 2
# Due Date: 05.09.21
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

def main():
    orders = int(input('\nEnter # of Orders: '))
    printHeader(orders)

    receipt = 0
    while orders > 0:
        receipt += 1
        print(f'\n**** *** ** Processing Order Ticket #{receipt} ** *** ****')
        entree, e_price = getEntree()
        side, s_price = getSide()
        drank = getDrank()
        if drank == 4:
            size = ""
            d_price = h2o
        else:
            size, d_price = getSize()

        if receipt == 1:
            file = open('receipt.txt', 'w')
        else:
            file = open('receipt.txt', 'a')
        file.write(f'\n--------------- Total for Order #{receipt} ---------------\n')
        file.write(f'{entree:<30}${e_price:<.2f}\n')
        file.write(f'{side:<30}${s_price:<.2f}\n')
        file.write(f'{(size + drank):<30}${d_price:<.2f}\n')

        orders += -1

    file.close()

def printHeader(num):
    print('\n*** *** *** *** *** Welcome *** *** *** *** ***')
    print('\n**** *** *** Binary Burger Program *** *** ****\n')

    print("\t\t 5112 E. MLK BLVD")
    print("\t\tLONG BEACH, CA 90806 ")
    print("\t\t    503.323.2342\n")
    print("Server: Kim Davis \t\t\t03/21/21")
    print(f"Guests: {num}\t\t\t\t11:11 AM")

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
    side = int(input('\nEnter\t[1] for a French Fries,\n\t[2] for Onion Rings,\n\t[3] for a Side Salad,\n\t[4] for No Side..\n\nYour Selection: '))
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
def getDrank():
    drink = int(input('\nEnter\t[1] for Coke\n\t[2] for Sprite\n\t[3] for Lemonade\n\t[4] for Water\n\nYour Selection: '))

    if drink == 1: # Coke Selected
        drank = 'Coke'
    elif drink == 2: # Sprite Selected
        drank = 'Sprite'
    elif drink == 3: # Lemonade Selected
        drank = 'Lemonade'
    elif drink == 4: # Water Selected
        drank = 'Water Cup'
    else: 
        getDrank()

    return drank

## Size function: getSize()
def getSize():
    size = int(input('\nEnter\t[1] for Small\n\t[2] for Medium\n\t[3] for Large\n\nYour Selection: '))
    if size == 1:
        drink_size = 'Small '
        drink_price = 1.50
    elif size == 2:
        drink_size = 'Medium '
        drink_price = 2.25
    elif size == 3:
        drink_size = 'Large '
        drink_price = 2.75
    else:
        getSize()

    return drink_size, drink_price

# def getSubtotal():


main()


    