import random

f = open("words.txt", "r")
words = f.read().split("\n")
random_word = random.choice(words) 
print(random_word)

y = list("_"*len(random_word))
x = " ".join(y)
print(x)

while True:
    letter = input("Enter a letter you want to guess: ").upper()
    
    for i in range(len(random_word)):
        if letter == random_word[i]:
            y[i] = letter
    print(" ".join(y))
    
    if letter in(" ".join(y)):
            print("You already guessed that letter. Try again.")
            continue
    
    if random_word == 
         print("You guessed the word!!")
         break
