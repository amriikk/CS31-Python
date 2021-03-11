##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch2_HW
# Due Date: 02.21.21
# ####################################################

# 12. Stock Transaction Program

num_Shares = 2000 # num of stocks purchased
stock_Price = 40.00
purchase_Amount = num_Shares * stock_Price 
p_commission = purchase_Amount * 0.03 # stock purchase commission
net_Purchase = purchase_Amount - p_commission

    ## two weeks later..

sell_Price = 42.75 # stock price per share sold
sell_Amount = num_Shares * sell_Price
s_commission = (num_Shares * sell_Price) * 0.03

print(f'Total Amount "Joe" paid for the stock: ${purchase_Amount:,.2f}')
print(f'Commission Amount "Joe" paid for the purchased stock: ${p_commission:,.2f}')
print(f'$ Amount sold by "Joe" for the stock (pre-commission): ${sell_Amount:,.2f}')
print(f'Commission paid for the sold stock: ${s_commission:,.2f}')

net_Profit = (sell_Amount - purchase_Amount) - (p_commission + s_commission)
print(f'Net profit for sold stock (after commissions): ${net_Profit:,.2f}')

if net_Profit > 0:
    print(f"Joe made a Net Profit of ${net_Profit:,.2f} :D")
else: 
    print("Joe made NO MONEY$ :(\n")


# 13. Planting Grapevines

R = float(input("Enter length of row (in feet): "))
E = float(input("Enter the amount of space (in feet), used by an end-post assembly: "))
S = float(input("Enter the space between the vines (in feet): "))

V = (R - 2*E)/S

print(f"{V:.2f} grapevines fit in this row.")
print()


# 14. Compound Interest

P = float(input("Enter the amount of the principal originally deposited into account: "))
rate = float(input("Enter interest rate (as a %): "))
r = rate / 100
n = float(input("Enter # of times per year that the interest is compounded (e.g. if interest is compounded monthly; enter 12, if quarterly; enter 4.) "))
t = float(input("Enter # of years the account will be left to earn interest: "))

A = P*(1 + (r/n)) ** (n*t)

print(f"Total amount of money in the account after {t} year(s): ${A:.2f}")