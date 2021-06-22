import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Apolodizem, guess again. Its too low')
        elif guess > random_number:
            print('Apologize, guess again. Its too high')

    print(f'Yay, Congrats. You have guessed the number {random_number} correctly.')

def computer_guess(X):
    low = 1
    high = X
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correctly')            
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low == guess + 1

    print(f'Yes !! The computer guessed your number, {guess}, correctly!')


computer_guess(100)