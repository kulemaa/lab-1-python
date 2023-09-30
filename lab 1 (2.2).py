number = int(input("Type a four-digit number: "))

if 1000 <= number <= 9999:

    thousands = number // 1000
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    ones = number % 10

    print("The digit in the thousands position is:", thousands)
    print("The number in the hundreds position is:", hundreds)
    print("The digit in the tens position is:", tens)
    print("The digit in the position of units is:", ones)
else:
    print("Wrong.")