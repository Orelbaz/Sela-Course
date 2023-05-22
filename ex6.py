#asking the user for a "string" and checking if the string is a palindrome

str = input("Enter a string: ")

print(str[::-1])

if str == str[::-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")