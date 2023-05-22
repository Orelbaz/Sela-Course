a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
#prints all the numbers that are less than 5 in 1 line

for num in a:
    if num < 5:    
        print(num)
        b.append(num)
print(b)

#prints all the numbers that are less than user_number

usr_number = int(input("Enter a number: "))
new_list = [num for num in a if num < usr_number]

print(new_list)