# Caesar Cipher Implementation

This project implements a Caesar cipher, a classical encryption technique, in Python. The program allows users to encrypt or decrypt text using a specified shift value while preserving case sensitivity and non-alphabetic characters.

---

## Features
- Supports both **encryption** and **decryption**.
- Handles both **uppercase** and **lowercase** letters.
- Preserves non-alphabetic characters (e.g., spaces, punctuation).
- Allows repeated operations until the user decides to exit.

---

## How It Works
The Caesar cipher shifts each letter in the input text by a specified number of positions in the alphabet. The shift wraps around the alphabet (e.g., shifting `z` by 1 results in `a`).

### Encryption
Each letter is shifted **forward** by the specified shift value.

### Decryption
Each letter is shifted **backward** by the specified shift value.

---

## Usage

### Input
1. **Shift Value**: Enter the number of positions to shift (e.g., `3`).
2. **Command**: Choose whether to encrypt or decrypt:
   - `1` for encryption.
   - `2` for decryption.
3. **Text**: Enter the text to encrypt or decrypt.

### Output
The program displays the result of the encryption or decryption.

### Example
#### Input:
Enter a shift value: 3 What do you want to do?
1. Encrypt
2. Decrypt 
1 

Enter what you want to encrypt or decrypt: 
Hello, World!

#### Output:
The encryption for 'Hello, World!' is: Khoor, Zruog!

---

## Code Explanation
### `letters`
The `letters` variable contains all lowercase and uppercase English letters:
`letters` = ***string.ascii_lowercase + string.ascii_uppercase***

#### `caesar_cipher Function`
This function performs the encryption or decryption:

#### Parameters:
* `char`: The input text.
* `shift`: The shift value.
* `operation`: Either "encryption" or "decryption".

#### Logic:
1. For each character in the input:
2. If it is a letter, calculate the new index based on the shift value.
3. If it is not a letter, preserve it as is.
4. Return the transformed text.

### Main Program
1. `The program:`
    * Prompts the user for input (shift value, command, and text).
    * Calls the caesar_cipher function to process the text.
    * Displays the result.
    * Repeats the process until the user chooses to exit.

2. `Error Handling`
    * Ensures the shift value is a valid integer.
    * Validates the command input (must be 1 or 2).
    * Handles unexpected errors gracefully.

### Requirements
1. Python 3.x
2. No external libraries are required (uses the built-in string module).

### Future Improvements
1. Add support for custom alphabets or languages.
2. Implement a graphical user interface (GUI).
3. Add unit tests for better reliability.
