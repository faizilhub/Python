import random

number = random.randint(1, 20)
guesses = 0

print('I am thinking of a number between 1 and 20.')

while guesses < 6:
    print('Take a guess:')
    guess = input()
    guess = int(guess)

    guesses += 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    print(f'Good job! You guessed my number in {guesses} guesses.')

if guess != number:
    print(f'Nope. The number I was thinking of was {number}.')
