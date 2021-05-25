import Car

def main():
    myCar = Car.Car('2016', 'Subaru', 'Outback') # Calls function
    print(myCar) # calls the string function
    for x in range(5):
        myCar.accelerate()
        print('Now speed is ', myCar.how_fast(), 'MPH.')

    for x in range(5):
        myCar.brake()
        print('Now speed is ', myCar.how_fast(), 'MPH.')

main()