
secret_word = "mosiah"
guess_count = 0

underscore = "_" * len(secret_word)

print("Welcome to word guessing game!")
print()
user_guess = underscore

while user_guess != secret_word:
  print(f"Your hint is:", end="")
  if len(user_guess) == len(secret_word):
     for i in range(len(user_guess)):
      if user_guess [i] == secret_word [i]:
       print(user_guess[i].upper(), end="")
      elif user_guess[i] in secret_word:
        print(user_guess[i].lower(),end="")
      else:
        print("_", end="")
  else:
    print(f"The secret word  has {len(secret_word)} letter. Try again")
  print()
  user_guess = input("What is your guess?")
  guess_count += 1

else :
 (user_guess == secret_word)
 print("Congrats! You got that")


    #user_guess = input("Guess a letter: ").lower()
    #guess_count += 1

    

#else:
"""
       
          print(guess[i], end="")
      else:
          print("_", end="")
      print("\n")"""

print(f"it took you {guess_count} guesses")