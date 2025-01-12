# Caesar Cipher Encoder/Decoder

This Python program allows you to encode or decode a string using the Caesar Cipher, a type of substitution cipher where each letter in the plaintext is shifted by a certain number of places down the alphabet.

## Features

- **Encoding**: Shift the letters in a string forward by a specified number of characters.
- **Decoding**: Shift the letters in a string backward to recover the original message.
- **Input Validation**: Ensures the shift value is an integer between 1 and 25, and the string length is between 1 and 26 characters.
- **Handles Special Characters**: Supports spaces, commas, periods, and apostrophes in the input string.

## Requirements

- Python 3.x

## How to Use

1. **Run the program**.
2. You will be prompted with instructions to either encode or decode a string.
   - To encode a string, type `encode` or `e`.
   - To decode a string, type `decode` or `d`.
   - To exit the program, type `stop` or `s`.
3. When encoding or decoding, the program will ask you to:
   - Enter the string you'd like to encode or decode.
   - Provide the number of characters by which you'd like to shift the string.
4. The program will print the resulting encoded or decoded message.

### Example:

```plaintext
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

Please type 'encode' or 'e' to start encode or 'd' to 'decode' and 'stop' or 's' to stop: encode
Enter the string you would like to encode: Hello, World!
How many characters would you like to shift: 3
Encoded message: Khoor, Zruog!

