#!Dragons
import time
from random import randint
def intror():
    print('''
    Вы летите на своём драконе в туман. Вдруг из неоткуда появляется гора.
    Вы решили подойти к пещерам что таятся у подножья горы
    ''')
def introe():
    print('''
    You fly on your dragon in fog. Now you see a mountain afront.
    You decied to go in the caves.
    ''')
def choosee():
    cave = 0
    
    while cave != '1' and cave != '2':
        print("Choose your cave")
        cave = input("1 or 2: ")
    return(cave)
def chooser():
    cave = 0
    
    while cave != '1' and cave != '2':
        print("Выбери свою пещеру")
        cave = input("1 или 2: ")
    return(cave)
def cavee(cave):
    print('''
    You see the dragon, he open mouth and
    ''')    
    print('.',end = '')
    time.sleep(2)
    print('.',end = '')
    time.sleep(2)
    print('.',end = '')
    time.sleep(2)
    angrycave = randint(1,2)
    angrycave = str(angrycave)
    if angrycave == cave:
        print("Eat you")
    else:
        print("Give you a treasure")
def caver(cave):
    print('''
    Ты видешь дракона, он открывает пасть и
    ''')
    print('.',end = '')
    time.sleep(2)
    print('.',end = '')
    time.sleep(2)
    print('.',end = '')
    time.sleep(2)
    angrycave = randint(1,2)
    angrycave = str(angrycave)
    if angrycave == cave:
        print("Cъедает тебя")
    else:
        print("Даёт тебе сокровища")

print("rus or eng language?")
language = input("type rus or eng: ")
if language == "eng":
    introe()
    cave = choosee()
    cavee(cave)
elif language == "rus":
    intror()
    cave = chooser()
    caver(cave)
else:
    print("Restart programm and correctly choose language")
