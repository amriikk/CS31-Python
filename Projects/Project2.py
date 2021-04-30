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

        entree, entree_price = getEntree()
        print(f'Entree: {entree}\t\tPrice: ${entree_price:.2f}')

        orders += -1
    

## def for getEntree()
def getEntree():
    entree = int(input('\nEnter\t[1] for a Hamburger\n\t[2] for a Cheeseburger\n\t[3] for a Chicken Sandwich,\n\t[4] for no sandwich..\n\nYour Selection: '))
    
    if entree == 1:
        sammich = 'Hamburger'
        entree_price = hamburger
        return sammich, entree_price
    elif entree == 2:
        sammich = 'Cheeseburger'
        entree_price = cheeseburger
        return sammich, entree_price
    elif entree == 3:
        sammich = 'Chkn-Sandwich'
        entree_price = sandwich
        return sammich, entree_price
    elif entree == 4:
        sammich = 'no sammich'
        entree_price = 0
        return sammich, entree_price
    else:
        print('Invalid Entry')
        getEntree()

    

## def for getSide()

## def for getDrank()

main()