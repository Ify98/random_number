import random

feedback = str()
low = 0
high = 1000
c = 'correct'


def  system_guess():

    feedback = " "

while feedback != 'c':
    if low != high:
        guess = random.randint(low, high)
    else:
        guess = high
    feedback = input( f'is {guess} too high (H), too low (L), or correct (C)? ').lower()

    if  guess == high:
        high = guess - 1
    elif guess == low:
        low = guess + 1
else:
    print(f'Congrats, you guessed the secret number {guess} correctly')

system_guess()
