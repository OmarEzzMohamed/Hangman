from data import words, HANGMANPICS
import random



def guess(word, mistakes):
    if mistakes > -1:
        print(HANGMANPICS[mistakes])
    print
    
    if mistakes == 7:
        print('''==========
              Game Over
              ==========''')
    else:
        mistakes += 1
        guess(word, mistakes)
    
def round() :
    word = random.choice(words)
    wordLen = len(word)
    mistakes = -1
    
    guess(word, mistakes)
    
    


def main():
    points = 0
    print(f'''============
          ---Hangman---
          ============
            Ponits: {points}''')
    round()
    
if __name__ == "__main__":
    main()