
## Problem 19 - Future Value

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

