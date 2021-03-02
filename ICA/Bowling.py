# ICA1, Part 1 and 2

game_1 = int(input("Enter bowling score for game 1: "))
game_2 = int(input("Enter bowling score for game 2: "))
game_3 = int(input("Enter bowling score for game 3: "))

avg = (game_1 + game_2 + game_3) / 3

print(f'Your average for the three games is {avg:.1f}')

if avg >= 100:
    print("Bowling average meets requirement")
    print("Join league now")
else:
    print("Bowling avergage is too low")
    print("Sign Up for bowling classes")

# Part 3

word_1 = input("Enter a word with no spaces in it: ")
word_2 = input("Enter another word with no spaces in it: ")

if word_1 > word_2:
    print(word_1, "is greater than", word_2)
else:
    print(word_2, "is greater than", word_1)
