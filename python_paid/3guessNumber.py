import random
secretNumber=random.randint(1,20)
print('I an thingking of a number between 1 and 20.')

for guessesTaken in range(1,7):
    print("Take a guess.")
    guess=int(input())

    if guess < secretNumber:
        print('You guess is too low.')
    elif guess > secretNumber:
        print('You guess is too hight.')
    else:
        break

if guess == secretNumber:
    print('Good job!You guessed my number in '+str(secretNumber) + ' guesses!use '+str(guessesTaken)+' times!')
else:
    print('Nope.The number I was thinking of was '+str(secretNumber))