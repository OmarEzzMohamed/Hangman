from data import words, HANGMANPICS
import random

def main():
    points = 0
    print('''=============
---Hangman---
=============
Points: {}
============='''.format(points))

    # Start of a game
    while True:
        # round = word
        y = round(points)
        if y:  # Win Round
            points += 1
            print('''Points: {}
============='''.format(points))
        else:  # Lose Round
            print('''=============
Game Over
=============
Points: {}
============='''.format(points))
            exit()

def round(points):
    word = random.choice(words)
    word_guess = ["_" for _ in range(len(word))]
    wrong = set()  # To show Wrong letters
    lives = -1
    
    # Start of a guess
    while True:
        if lives > -1:
            print(HANGMANPICS[lives])
            
        if word == "".join(word_guess):  # If user got the word right
            print('''Good Job!
=============''')
            return 1
        
        print(" ".join(word_guess), end="")
        if wrong:
            print()
            print("Wrong: {}".format(', '.join(wrong)), end="")
        print("\n=============")
        u_guess = input("Guess a letter: ")
        
        if u_guess in word and u_guess not in word_guess:  # Letter has been written once
            print('''=============
Right Guess!
=============''')
            for i in range(len(word)):
                if word[i] == u_guess:
                    word_guess[i] = u_guess
        else:  # Wrong Guess
            if lives == 5:  # Game Over
                print('''==============
{}
Word: {}'''.format(HANGMANPICS[6], word))
                return 0
            else:  # Retry
                lives += 1
                wrong.add(u_guess)
                print('''=============
Wrong Guess! | {} tries left'''.format(6 - lives))

if __name__ == "__main__":
    main()
