num = int(input("Enter a number: "))
print("The divisors of", num, "are:")

# loop from 1 to num to check for divisors

for i in range(1, num+1):
   if num % i == 0:
      print(i)
