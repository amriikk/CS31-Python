# Week 5 - ICA 2

CONVERT_KM_TO_MI = 0.6214
CAL_FAT = 9
CAL_CARB =4

def main():
    kms = float(input('Enter kilometers: '))
    getMiles(kms)
    
    fatGrams = int(input('\nEnter fat grams consumed today: '))
    carbGrams = int(input('Enter carbohydrate grams consumed today: '))
    getCalories(fatGrams, carbGrams)

def getMiles(k):
    miles = k * CONVERT_KM_TO_MI
    print(f'{k:.1f} kilometers = {miles:.1f} miles.')

def getCalories(fat, carb):
    fat_calories = fat * CAL_FAT
    carb_calories = carb * CAL_CARB
    total_cals = fat_calories + carb_calories
    print('\nConsuming', fat, 'fat grams gives you', fat_calories, 'calories from fat.')
    print('Consuming', carb, 'carb grams gives you', carb_calories, 'calories from carbs.')
    print('Total calories from fat and carbs today is', total_cals)

main()