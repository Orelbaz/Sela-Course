birthdays = {
    "LeBron James": "December 30, 1984",
    "Kevin Durant": "September 29, 1988",
    "Stephen Curry": "March 14, 1988",
    "Kawhi Leonard": "June 29, 1991",
    "Giannis Antetokounmpo": "December 6, 1994"
}



print('Welcome to the birthday dictionary. We know the birthdays of:')
for key in birthdays:
    print(key)

print('Who\'s birthday do you want to look up?')
player = input()

print(f'{player}\'s birthday is {birthdays[player]}')