import math


def is_prime():
    PRIME = int(input('Enter a number:'))
    for num in range(2, int(math.sqrt(PRIME)) + 1):
        if PRIME % num == 0:
            return 'a loser number'
        else:
            return 'a PRIME number'


print(is_prime())