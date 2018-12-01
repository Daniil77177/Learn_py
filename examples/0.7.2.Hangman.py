import time
import random

print("Hangman")
print("")

arrayw = "акула зуб мир человек машина якорь зверь самолёт коготь книга обложка ручка наушники лампочка цветок собака яхта штора тетрадь олень листва".split() #Wordlist

#Create def, it choose random word and return it
def randomintegger():
    randomword = random.randint(0,len(arrayw) -1)
    randomword = arrayw[randomword]
    return randomword

hangman = [
    '''
    ----
        |
        |
        |
        |
    ------
''', '''
    ----
      O |
        |
        |
        |
    ------
''', '''
    ----
      O |
      | |
        |
        |
    ------
''', '''
    ----
      O |
     /|\|
        |
        |
    ------
''', '''
    ----
      | |
      O |
     /|\|
     / \|
    ------
'''
]
replay = 1
while replay == 1:
    turns = 0
    #Main

    random_word = randomintegger()
    s_random_word = "*" * len(random_word) #Generate "*" instead of letter
    win = False #If variable win = True, game is over, player win
    #Game beginning

    while turns != 5:
        print(hangman[turns])
        print("Your word is:")
        print(s_random_word) 
        print("Please, enter your letter: ", end="")
        user_l = input()
        continue1 = False #If continue = True, turns will not add 1
        for letterindexword in range(0, len(random_word)): #Check every letter in word
            if random_word[letterindexword] == user_l: #Check if letter identical with input
                continue1 = True
                srandomfast = list(s_random_word)
                srandomfast[letterindexword] = random_word[letterindexword]
                s_random_word = "".join(srandomfast)

        if continue1 == False:
            turns += 1

        if s_random_word == random_word: #If secret_word(*) = random_word(real word), player win
            print("You win, word is "+ random_word)
            win = True
            break

    if win == False: #After 5 turn cycle over, and if win = False, player lose
        print('''
        ''')
        print("You lose, try again")
        print("Word is "+ random_word)
    print("")
    print("Try again? (yes or no) ", end ="") #Try again block of code
    replay_user = input()

    if replay_user.lower() == "no":
        exit()
