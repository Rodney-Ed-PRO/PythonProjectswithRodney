from replit import clear
import random 

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

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(chosen_word)

display = []
for _ in range(word_length):
    display += "_"
print(display)


# while "_" in display:
while not end_of_game:
    guess = input("What letter would you like to guess? ").lower()
    clear()
    # counter = -1
    # for char in chosen_word:
    #     counter += 1
    #     if guess == char:
    #         print("You guessed the right letter!")
    #         display[counter] = guess
    #     else: 
    #         print("That letter is not in the word. Try again!")
    if guess in display:
        print(f"You've already guessed {guess}.")
    # print(counter)
    for position in range(word_length):
        if guess == chosen_word[position]:
            display[position] = guess
    if guess not in chosen_word:
        print(f"You guessed {guess}.That's not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Game Over. You lost.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You won!")
    print(f"You have {lives} lives remaining.")
    print(stages[lives])
        
   
