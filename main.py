import os


def clear():
    """Clears the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def valid_digit(entry):
    """Check if the input is valid

    Args:
        entry (int): User input to be verified

    Returns:
        Bool: True if all digits are valid, False if not
    """
    for i in str(entry):
        if i == '0' or i == '1':
            continue
        else:
            return False
    return True


def user_entry():
    """Wait for user input and checks for irregularities

    Returns:
        int: Return user entry
    """
    print('Insert up to 8 binary digits.\n')
    try:
        entry = int(input('>>>>> '))
        print()
        if len(str(entry)) <= 8 and valid_digit(entry):
            return entry

        else:
            print('Insert 8 binary digits maximum\n')
            user_entry()

    except ValueError:
        print('Insert binary digits\n')
        user_entry()


def binary_converter(entry):
    """Converts binary digits to decimal digits

    Args:
        entry (int): Receive digits from user input

    Returns:
        int, int: Returns binary digits, decimal digits
    """
    dec = 0
    power = len(str(entry))
    for i in str(entry):
        dec += int(i) * (2 ** (power - 1))
        power -= 1
    return entry, dec


if __name__ == '__main__':
    clear()
    binary, decimal = binary_converter(user_entry())
    clear()
    print(f'Binary: {binary}')
    print(f'Decimal: {decimal}')
