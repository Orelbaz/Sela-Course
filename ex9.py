#the system choosing a random number between 1-9
import random
random_num = random.randint(1, 9)

#number of input guessed
num_guess = 0

#asking the user to guess a number between 1-9 and -1 is for giving up
while True:
 guess_num = int(input("Guess a number: "))
#every loop adding 1 to the guess list
 num_guess += 1
 if guess_num == -1:
    break
 elif guess_num >=1 and guess_num <= 9:
  pass
 else: 
   input("You must pick a number between 1 to 9")

 if guess_num < random_num:
    print("You guessed to low")
 if guess_num > random_num:
    print("You guessed to high")
 if guess_num == random_num:
    print ("Bingo!!") 
    break

print(num_guess)
  

