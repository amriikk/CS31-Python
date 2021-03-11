# Week 5 - ICA 2

def main():
    kms = float(input('Enter kilometers: '))
    getMiles(kms, convert=0.6214)
    print()
    fatGrams = int(input('Enter fat grams consumed today: '))
    carbGrams = int(input('Enter carbohydrate grams consumed today: '))
    getCalories(fatGrams, carbGrams, fconv=9, cconv=4)

def getMiles(k, convert):
    miles = k * convert
    print(f'{k:.1f} kilometers = {miles:.1f} miles.')

def getCalories(fat, carb, fconv, cconv):
    fat_calories = fat * fconv
    carb_calories = carb * cconv
    total_cals = fat_calories + carb_calories
    print('\nConsuming', fat, 'fat grams gives you', fat_calories, 'calories from fat.')
    print('Consuming', carb, 'carb grams gives you', carb_calories, 'calories from carbs.')
    print('Total calories from fat and carbs today is', total_cals)


main()