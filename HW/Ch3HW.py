##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch3_HW
# Due Date: 03.01.21
# ####################################################

print("Enter two DISTINCT Primary Colors. (Enter selections in lowercase letters): ")

color1 = (input("Enter your first primary color: "))
color2 = (input("Enter a different primary color: "))

bad = color1 != "red" and color1 != "yellow" and color1 != "blue" and \
      color2 != "red" and color2 != "yellow" and color2 != "blue"
if bad:
    print("You must enter PRIMARY colors. Check your spelling and case.")
elif color2 == color1:
    print("You must enter two DISTINCT primary colors.")
elif color1 == "red" and color2 == "yellow":
    print("When mixed, the colors you chose create orange.")
elif color1 == "yellow" and color2 == "red":
    print("When mixed, the colors you chose create orange.")
elif color1 == "red" and color2 == "blue":
    print("When mixed, the colors you chose create purple.")
elif color1 == "blue" and color2 == "red":
    print("When mixed, the colors you chose create purple.")
elif color1 == "blue" and color2 == "yellow":
    print("When mixed, the colors you chose create green.")
else:
    print("When mixed, the colors you chose create green.")
print()