def caesar_encode():
    # Function to encode message
    str1ng = input("Enter the string you would like to encode: ")

    while True:
        try:
            val = int(input("How many characters would you like to shift: "))
            if val < 1 or val > 25:  # Check if shift is between 1 and 25
                print("Please enter a value between 1 and 25.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 25.")

    char = ''
    for _ in str1ng:
        if _.isupper():
            char += chr((ord(_) + val - 65) % 26 + 65)
        elif _.islower():
            char += chr((ord(_) + val - 97) % 26 + 97)
        elif _ in [' ', '.', ',', "'"]:
            char += _

    print(f"Encoded message: {char}")


def caesar_decode():
    # Function to decode message
    str1ng = input("Enter the string you would like to decode: ")

    while True:
        try:
            val = int(input("How many characters was string shifted: "))
            if val < 1 or val > 25:  # Check if shift is between 1 and 25
                print("Please enter a value between 1 and 25.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 25.")

    char = ''
    for _ in str1ng:
        if _.isupper():
            char += chr((ord(_) + (26 - val) - 65) % 26 + 65)
        elif _.islower():
            char += chr((ord(_) + (26 - val) - 97) % 26 + 97)
        elif _ in [' ', '.', ',', "'"]:
            char += _

    print(f"Decoded message: {char}")


if __name__ == '__main__':

    print("""
    Welcome to the Caesar Cipher Encoder/Decoder!

    This program will allow you to:
    - Encode a string by shifting its letters forward.
    - Decode a string by shifting its letters backward.

    Important:
    - The string length must be between 1 and 26 characters.
    - The shift value must be between 1 and 25 (inclusive).

    To get started:
    - Type 'encode' or 'e' to encode a string.
    - Type 'decode' or 'd' to decode a string.
    - Type 'stop' or 's' to exit the program.
    """)

    while True:
        print('\n')
        answer = input('Please type \'encode\' or \'e\' to start encode or \'d\' to \'decode\' and \'stop\' or \'s\' to stop: ')
        answer = answer.lower()
        if answer == 'encode' or answer == 'e':
            caesar_encode()
        elif answer == 'decode' or answer == 'd':
            caesar_decode()
        else:
            break