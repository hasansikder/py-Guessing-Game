import random
for x in range(1, 6):
    guessNumber = int(input("Enert your Number= "))
    randomNumber = random.randint(1, 5)
    if guessNumber == randomNumber:
        print("You have won")
    else:
        print("You have lost")

    print(randomNumber)
