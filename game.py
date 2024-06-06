from data import words, HANGMANPICS
import random

def main():
    points = 0
    print(f'''=============
---Hangman---
=============
Points: {points}
=============''')
    # Start of a game
    while 1:
        # round = word
        y = round(points)
        if y : # Win Round
            points +=1
            print(f'''=============
Points: {points}
=============''')
        else: # Lose Round
            print(f'''=============
Game Over
=============
Points: {points}
=============''')
            exit()
    
def round(points):
    word = random.choice(words)
    word_guess = [*len(word)*"_"]
    wrong = set() # To show Wrong letters
    lives = -1
    # Start of a guess
    while 1:
        if lives > -1:
            print(HANGMANPICS[lives])
        if word == "".join(word_guess): # If user got the word right
            print(f'''=============
Good Job!
=============''')
            return 1
        print(" ".join(word_guess), end="")
        if wrong:
            print()
            print(f"Wrong: {', '.join(wrong)}", end="")
        print("\n=============")
        u_guess = input("Guess a letter: ")
        if u_guess in word and u_guess not in word_guess: # Letter has been written once
            print('''=============
Right Guess!
=============''')
            for i in range(len(word)):
                if word[i] == u_guess:
                    word_guess[i] = u_guess
                
        else: # Wrong Guess
            if lives == 5: #Game Over
                print(f'''==============
{HANGMANPICS[6]}
Word: {word}''')
                return 0
            else: # Retry
                lives +=1
                wrong.add(u_guess)
                print(f'''=============
Wrong Guess! | {6-lives} tries left''')
            

if __name__ == "__main__":
    main()
