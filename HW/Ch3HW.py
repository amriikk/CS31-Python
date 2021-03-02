##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch3_HW
# Due Date: 03.01.21
# ####################################################

# 7 -- Color Mixer

# print("Enter 2 Primary Colors: ")
# color1 = input("\tEnter 1st primary color: ").lower()
# color2 = input("\tEnter 2nd primary color: ").lower()

# print()

# BAD = color1 != "red" and color1 != "yellow" and color1 != "blue" and \
#       color2 != "red" and color2 != "yellow" and color2 != "blue"

# if BAD: # Boolean Variable
#     print("You must enter PRIMARY colors. Please try again!")
# elif color2 == color1:
#     print("You must enter two DISTINCT primary colors. ")
# elif color1 == "red" and color2 == "blue":
#     print("Red + Blue => Purple.")
# elif color1 == "blue" and color2 == "red":
#     print("Blue + Red => Purple.")
# elif color1 == "red" and color2 == "yellow":
#     print("Red + Yellow => Orange.")
# elif color1 == "yellow" and color2 == "red":
#     print("Yellow + Red => Orange.")
# elif color1 == "blue" and color2 == "yellow":
#     print("Blue + Yellow => Green.")
# else:
#     print("Yellow + Blue => Green.")

# print('\n')

# 9 -- Roulette Wheel Colors

num = int(input('Enter a pocket number from 0 - 36: '))

if num < 0 or num > 36:
    print('Please enter a valid number !')
elif num == 0:
    print('Pocket is GREEN!')
elif 1 <= num <=10:
    if num % 2 == 0:
        print('Pocket is BLACK!')
    else:
        print('Pocket is RED!')
elif 11 <= num <=18:
    if num % 2 == 0:
        print('Pocket is RED!')
    else:
        print('Pocket is BLACK!')
elif 19 <= num <=28:
    if num % 2 == 0:
        print('Pocket is BLACK!')
    else:
        print('Pocket is RED!')
elif 29 <= num <=36:
    if num % 2 == 0:
        print('Pocket is RED!')
    else:
        print('Pocket is BLACK!')
else:
    print('Please try your input again! ')

print() # End of Roulette Wheel Colors

# 12 -- Software Sales

print() # End of Software Sales