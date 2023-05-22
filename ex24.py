import sys

i = int(input("Enter what size game board you want to draw: "))
counter = 0

while (counter!=i):
    print("--- " * i)
    print("| | " * i)
    print("--- " * i)
    counter += 1
    
print("I finished")

