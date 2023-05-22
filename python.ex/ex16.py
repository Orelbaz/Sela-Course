import random
import string

def weak_passwd(length):   
    return ''.join(random.choice(string.ascii_letters) for x in range(length))

def strong_passwd(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for x in range(length))
    return random_string

choise = input("Enter 's' for strong password or 'w' for weak password: ")

if choise == 's':
    print(strong_passwd(10))
if choise == 'w':
    print(weak_passwd(3))