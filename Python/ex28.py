
number1 = int(input('enter your first number: '))
number2 = int(input('enter your second number: '))
number3 = int(input('enter your third number: '))


def max(number1, number2, number3):
    if number3 < number1 > number2:
        return number1
    if number3 < number2 > number1:
        return number2
    if number1 < number3 > number2:
        return number3





print(max(number1, number2, number3))