import random

randomnum = random.randint(1, 20)

print("Guess the number, you'll have 3 takes")

for guess in range(3):
    urguess = int(input("Guess the number: "))

    if urguess == randomnum:
        break
    
    if urguess < randomnum:
        print("Ur number smalller than our number")
    
    if urguess > randomnum:
        print("Ur number bigger than our number")

if urguess == randomnum:
    print("Excellent! You did it in", guess + 1, "take(s)")

if urguess != randomnum:
    print("My number is", randomnum)
