

def caesar_encode():
    #Function to encode message
    str1ng = input("Enter the string you would like to encode: ")
    val = int(input("How many characters would you like to shift: "))
    if val < 0 or val > 26:
        print('Please enter a value between 1 and 26: ')
        return
    char=''
    temp=0
    for _ in str1ng:
        if _.isupper():
            char += chr((ord(_) + val-65) % 26 + 65)
        if _.islower():
            char += chr((ord(_) + val-97) % 26 + 97)
        if _ == ' ' or _ == '.' or _ == ',' or _ == "'":
            char += _
        else:
            continue
    print(char)

def caesar_decode():
    #Function to decode message
    str1ng = input("Enter the string you would like to decode: ")
    val = int(input("How many characters was string shifted: "))
    if val < 0 or val > 26:
        print('Please enter a value between 1 and 26: ')
        return
    char=''
    temp=0
    for _ in str1ng:
        if _.isupper():
            char += chr((ord(_) + (26-val)-65) % 26 + 65)
        if _.islower():
            char += chr((ord(_) + (26-val)-97) % 26 + 97)
        if _ == ' ' or _ == '.' or _ == ',' or _ == "'":
            char += _
        else:
            continue
    print(char)

if __name__ == '__main__':

    print("""Function will use the Caesar cipher to encode or decode a string. Enter the string and the characters to shift.
    Value should be between 1 - 26. """)

    while True:
        print('\n')
        answer = input('\'encode\' or \'e\' to start encode or \'d\' to \'decode\' and \'stop\' or \'s\' to stop: ')
        answer = answer.lower()
        if answer == 'encode' or answer == 'e':
            caesar_encode()
        elif answer == 'decode' or answer == 'd':
            caesar_decode()
        else:
            break


