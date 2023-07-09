import random
random_num = str(random.randint(1000, 9999))

#explain the game for the user
print("""Lets play cows and bulls 
i will Randomly generate a 4-digit number and ask you to guess the 4-digit number. 
For every digit you guessed correctly in the correct place, you have a cow.
For every digit you guessed correctly in the wrong place is a bull.""")

#number of trys
trys = 0
while True:
 user_guess = input("Enter a 4 digit number: ")
 trys += 1
 # check how many digits are correct and in the right place
 cows = 0
 for i in range(4):
    if user_guess[i] == random_num[i]:
     cows += 1
 
 # check how many digits are correct but in the wrong place
 bulls = 0
 for i in range(4):
    if user_guess[i] in random_num and user_guess[i] != random_num[i]:
     bulls += 1

 # output the result to the user
 if cows == 4:
    print("You won the game!!")
    break
 elif cows > 0 or bulls > 0:
    if cows > 0:
        print("You guessed", cows, "cows")
    if bulls > 0:
        print("You guessed", bulls, "bulls")
 else:
       print("You guessed no bulls or cows")

print("You won in", trys, "trys")
