a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#prints all the common numbers in the lines without duplication
c = []

for num in a:
    if num in b and num not in c:
        c.append(num)

print(c)