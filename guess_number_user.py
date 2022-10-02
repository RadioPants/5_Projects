import random  #random.randint(a, b) /Returns randInt 'N' such that a <= N <= b


def guess(x):
    random_number = random.randint(1, x) #randnumber to guess between 1 and x
    guess = 0 #guess must be between 1 and x (will never be zero)
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: ')) #Casts as int()
        if guess < random_number:
            print("Sorry bro, guess again. You're too low.")
        elif guess > random_number:
            print('Sorry, try again. Too high.')
    print(f'Nice, You guessed {random_number} correctly!')

guess(20) #Sets x /so guess random between 1 and x

#17 Down. Computer is guessing our random number:

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high b/c low = high
        guess = random.randint(low, high)
        feedback = input(f" Is {guess} too high (H), too ow (L), or correct (C)").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Computer guessed your number, {guess}, correctly!')

   guess(10)