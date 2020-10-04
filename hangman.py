import random
import json

HANGMAN_DRAWINGS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']



def getRandomWord():
    list = []
    for keys in data.keys():
        list.append(keys)
    f.close()
    num=random.randint(0,len(list))
    k = list[num].split()
    return(k[0])


def displayBoard(missedLetters, correctLetters, selectedWord):
    print(HANGMAN_DRAWINGS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    print('Correct letters:', end=' ')
    for letter in correctLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(selectedWord)

    for i in range(len(selectedWord)):
        if selectedWord[i] in correctLetters:
            blanks = blanks[:i] + selectedWord[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')

    print()


def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter:')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def wordMeaning():
    s=data.get(selectedWord)
    print(selectedWord+" means -",end=" ")
    print(s[0])
    print("\n")
    print("Do you want to play again?(yes or no)")
    return input().startswith('y' or 'Y')



print('W E L C O M E   T O   H A N G M A N')
f = open("data.json", )
data = json.load(f)
missedLetters = ''
correctLetters = ''
selectedWord = getRandomWord()
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, selectedWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in selectedWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(selectedWord)):
            if selectedWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('Yes! The secret word is "' + selectedWord +
                  '"! You have won!')
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess


    if len(missedLetters) == len(HANGMAN_DRAWINGS) - 1:
        displayBoard(missedLetters, correctLetters, selectedWord)
        print('You have run out of guesses!\nAfter ' +str(len(missedLetters)) +
              ' missed guesses and ' +str(len(correctLetters)) + ' correct guesses,the word was "' + selectedWord + '"')
        gameIsDone = True



    if gameIsDone:
        print("You can get the meaning of the word "+selectedWord+" by pressing k \n")
        print("Do you want to play again?(yes or no)")
        p=input().lower()
        if p=='k':
            l=wordMeaning()
            if l==False:
                break
            else:
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                selectedWord = getRandomWord()


        elif p.startswith('y' or 'Y'):
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            selectedWord = getRandomWord()

        else:
            break


