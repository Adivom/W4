#First part
"""magic_number = int(input("What is the magic number?  "))
guess_number = int(input("What is your guess? "))

if guess_number < magic_number:
    print('Higher')
elif guess_number > magic_number:
 print("Lower")
else:
    guess_number == magic_number
    print(" You Guessed it!!")"""

#Second Part
import random

magic_number = random.randint(1, 100)

keep_playing = "yes"
 

guess_count = 0

guess = -1

while guess != magic_number:
    guess = int(input("What is your guess? "))
    guess_count = guess + 1

    if guess < magic_number:
        print("Higher")
    elif guess > magic_number:
        print("Lower")
    else:
        print("You guessed it!")


print(f"it took you {guess_count} guesses")

while keep_playing == "yes":
  magic_number = random.randint(1, 100)
  keep_playing = input("Would you like to play again (yes/no)? ")

print("Thank you for playing. Goodbye.")


