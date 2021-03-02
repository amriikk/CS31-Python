################################################
# CS 31 - Kyle Muldrow
# Jhon Trujillo
# ICA - 1
# 02.17.2021
################################################


# ICA 1 , Part 1

# 6
STATE = 0.05    # State Tax
COUNTY = 0.025  # County Tax

amount = float(input("Enter purchase amount: "))
print()

state_tax = amount * STATE
county_tax = amount * COUNTY
total_tax = state_tax + county_tax
total_sale = amount + total_tax

print(f"Purchase amount: ${amount:.2f}")
print(f"State Sales Tax: ${state_tax:.2f}")
print(f"County Sales Tax: ${county_tax:.2f}")
print(f"Total Sales Tax: ${total_tax:.2f}")
print(f"Total Sale: ${total_sale:.2f}")
print()

# 8
TAX = 0.07
TIP = 0.18

check = float(input("How much was dinner? "))
print()


tip = check * TIP
tax = check * TAX
total = check + tax + tip

print(f"Check amount: ${check:.2f}")
print(f"Sales Sale: ${tax:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Total Sale: ${total:.2f}")
