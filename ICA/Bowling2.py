# ICA2, Part I

game_1 = int(input("Enter bowling score for game 1: "))
game_2 = int(input("Enter bowling score for game 2: "))
game_3 = int(input("Enter bowling score for game 3: "))

avg = (game_1 + game_2 + game_3) / 3

print(f'Your average is {avg:.1f}')

if avg >= 100:
    print("Bowling average meets requirement")
    if avg < 120:
        print("Join Beginner League")
    elif avg < 150:
        print("Join Intermediate league")
    else: 
        print("Join Advanced League")
else:
    print("Bowling average does not meet requirement..")

# Part 3

num = int(input("Enter a number between 1 and 7: "))
invalid_Num = num < 1 or num > 7 # Boolean variable

if invalid_Num:
    print("Invalid number")
elif num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")