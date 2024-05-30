#Step 1 
import random
import hangman_art, hangman_words
import os
import time
word_list = ["aardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(hangman_words.word_list)
letters = []
wrong_guesses =[]
lives = 6

print(hangman_art.logo)

# Create an empty list to hold correct guesses

for letter in chosen_word:
  letters.append('_')
print(f"\n{' '.join(letters)}")

while letters != list(chosen_word):
  guess = input("\nGuess a letter: ").lower()

  # Clear the console
  os.system('clear')
  print(f"{hangman_art.logo}\n")

  if guess in letters:
    print(f"\n'{guess}' has already been chosen. Please guess again!\n")
  # Add guess to correct guesses list
  if guess in list(chosen_word):
    for index, letter in enumerate(list(chosen_word)):
      if guess == letter:
        print(f"You have {lives} lives left.\n") 
        print(stages[lives])
        letters[index] = letter        
  else:
    if lives > 0: 
      if guess in wrong_guesses:
        print(f"You have {lives} lives left.\n") 
        print(stages[lives])
        print(f"\n'{guess}' has already been chosen. Please guess again!\n")
      elif guess == '':
        print(f"You have {lives} lives left.\n") 
        print(stages[lives])
        print("\nOops! You didn't chose a letter. Please try again.")
      else:
          wrong_guesses.append(guess)
          print(f"You have {lives} lives left.\n")
          print(stages[lives])
          print("\nWRONG")
          print(f"\n'{guess}' is not in the word!")
          lives -= 1
    else: 
      print(stages[lives])
      print("\nOh no! Your friend has died 😢!!")
      break

  print(' '.join(letters))

if letters == list(chosen_word):
  print("\nYOU WIN!!")





