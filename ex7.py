a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#checking the even numbers in a and prints then in a new list

new_list = [num for num in a if num % 2 == 0]
print(new_list, end=" ")