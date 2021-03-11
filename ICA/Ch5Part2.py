# Week 5 - ICA 2

def main():
    kms = float(input('Enter kilometers: '))
    getMiles(kms)

def getMiles(k):
    miles = k * 0.6214
    print(f'{k:.1f} kilometers = {miles:.1f} miles.')

main()