import random  #random.randint(a, b) /Returns randInt 'N' such that a <= N <= b

def guess(x):
    random_number = random.randint(1, x) #randnumber to guess between 1 and x
    guess = 0 #guess must be between 1 and x (will never be zero)
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: ')) #Casts as int()
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Nice, You guessed the number!!{random_number} correctly')

guess(20) #Sets x /so guess random between 1 and x