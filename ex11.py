import math

def prime_numbers(x):
    if x < 2:
        return False
    for i in range(2, math.isqrt(x) + 1):
        if x % i == 0:
            print(prime_numbers(9) "The number is not prime number")

    print(prime_numbers(9)"The number is prime number")
