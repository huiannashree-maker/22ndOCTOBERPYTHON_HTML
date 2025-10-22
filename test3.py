import random
print('=====Number Guessing Game======')

#step1
secret=random.randint(1,20)
attempts=0

#step2
guess=None
while guess !=secret:
    guess=int(input('Guess a number between 1 and 20: '))
    attempts+=1
    if guess<secret:
        print('too low!! Try again.\n')
    elif guess>secret:
        print('Too High!!! Try Again\n')
    else:
        print(f"Congratulations you guessed it right in {attempts} attempts.")
print('----------GAME OVER---------')