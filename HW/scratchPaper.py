
## Problem 19 

def main():
    P = float(input('Enter Acconut\'s Present Value: '))
    i = float(input('Enter Monthly Interest Rate (in percent):'))/100
    t = int(input('Enter # of Months: '))

    F =  futureValue(P, i, t)

    print(f'Future Value of the account ${F:,.2f} after a total of [{t}] Months')

def futureValue(pValue, mInterest, nMonths):
    fValue = pValue * (1 + mInterest) ** nMonths

    return fValue

## Solution 19
main()




# ## 19 

# P = float(input('Enter Acconut\'s Present Value: '))
# i = int(input('Enter Monthly Interest Rate: '))
# t = int(input('Enter # of Months: '))

# F = 

# def futureValue(pValue, mInterest, nMonths):
#     fValue = pValue * (1 + mInterest) ** nMonths

#     return fValue

