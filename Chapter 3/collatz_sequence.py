def collatz(number: int) -> int: 
    print(number)
    if number == 1:
        pass
    elif number % 2 == 0:
        return collatz(number // 2)
    elif number % 2 == 1:
        return collatz(3 * number + 1)

user_number = int(input('Please enter a number '))
try:
    collatz(user_number)
except ValueError:
    print('Please enter an integer value')