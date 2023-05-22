def find_largest(a, b, c):

    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c < a and c > b:
        return c
    
print(find_largest(5, 4, 1))
