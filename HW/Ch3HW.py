##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch3_HW
# Due Date: 03.01.21
# ####################################################

print("Enter 2 DISTINCT Primary Colors: ")

color1 = (input("Enter 1st primary color: ")).lower()
color2 = (input("Enter 2nd primary color: ")).lower()
# color1 = color1.lower()
# color2 = color2.lower()

print()

BAD = color1 != "red" and color1 != "yellow" and color1 != "blue" and \
      color2 != "red" and color2 != "yellow" and color2 != "blue"

if BAD: # Boolean Variable
    print("You must enter PRIMARY colors. Please try again!")
elif color2 == color1:
    print("You must enter two DISTINCT primary colors. ")
elif color1 == "red" and color2 == "yellow":
    print("Red + Yellow = Orange.")
elif color1 == "yellow" and color2 == "red":
    print("Yellow + Red = Orange.")
elif color1 == "red" and color2 == "blue":
    print("Red + Blue = Purple.")
elif color1 == "blue" and color2 == "red":
    print("Blue + Red = Purple.")
elif color1 == "blue" and color2 == "yellow":
    print("Blue + Yellow = Green.")
else:
    print("Yellow + Blue = Green.")
