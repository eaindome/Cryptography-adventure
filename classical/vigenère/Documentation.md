# Vigenère Cipher Implementation

## Overview
The Vigenère cipher is a method of encrypting alphabetic text by using a series of Caesar ciphers based on the letters of a keyword. It is a polyalphabetic substitution cipher that enhances security compared to simple substitution ciphers.

This implementation supports both **encryption** and **decryption** while maintaining case sensitivity.

## Features
- Supports both **uppercase** and **lowercase** letters.
- Ignores non-alphabetic characters while processing.
- Handles keyword repetition to match the length of the plaintext.
- Provides an interactive command-line interface for encryption and decryption.

## Usage
The script prompts the user for input, including the text to process and a keyword. It then asks whether the user wants to encrypt or decrypt the message and displays the result.

## Implementation Details

### Dependencies
The script uses Python's built-in `string` module for handling alphabetic characters.

```python
import string
```

### Alphabet Set
The program uses both lowercase and uppercase letters:

```python
letters = string.ascii_lowercase + string.ascii_uppercase
```

### Key Generation
To ensure the key matches the length of the text, it is repeated as necessary:

```python
def generate_key(text, keyword):
    filtered_text = "".join([char for char in text if char.isalpha()])
    key = keyword
    while len(key) < len(filtered_text):
        key += keyword
    return key[:len(filtered_text)]
```

### Vigenère Cipher Function
This function encrypts or decrypts text based on the selected operation:

```python
def vigenère_cipher(text, key, operation):
    newChar = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            is_lower = char.islower()
            text_index = letters.index(char)
            key_index_value = letters.index(key[key_index].lower()) % 26
            if operation == "encryption":
                new_index = (text_index + key_index_value) % 26
            elif operation == "decryption":
                new_index = (text_index - key_index_value + 26) % 26
            newChar += letters[new_index] if is_lower else letters[new_index].upper()
            key_index += 1
        else:
            newChar += char
    return newChar
```

### Interactive User Input
The program repeatedly prompts the user for text, keyword, and operation (encryption or decryption):

```python
another = True
while another:
    try:
        text = input("Enter your text:\n")
        keyword = input("Enter your keyword:\n")
        key = generate_key(text=text, keyword=keyword)

        command = int(input("What do you want to do?\n1. Encrypt\n2. Decrypt\n"))
        if command not in [1, 2]:
            raise ValueError("Invalid command. Please enter 1 for Encrypt or 2 for Decrypt.")
        
        operation = "encryption" if command == 1 else "decryption"
        
        result = vigenère_cipher(text=text, key=key, operation=operation)
        
        print(f"The {operation} for {text} is:\n{result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    again = int(input("Do you want to go again?\n1. Yes\n2. No\n"))
    if again == 2:
        another = False
```

## Example Usage
### Encryption Example
**Input:**
```
Text: HELLO
Keyword: KEY
```
**Output:**
```
The encryption for HELLO is: RIJVS
```

### Decryption Example
**Input:**
```
Text: RIJVS
Keyword: KEY
```
**Output:**
```
The decryption for RIJVS is: HELLO
```

## Notes
- The program maintains case sensitivity but only applies the cipher to alphabetic characters.
- Any non-alphabetic characters (spaces, numbers, punctuation) remain unchanged in the final result.

## Future Improvements
- Add support for extended character sets.
- Implement a graphical user interface (GUI) for ease of use.
- Enhance error handling for robustness.

