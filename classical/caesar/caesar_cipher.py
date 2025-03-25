import string

# letters with now both lowercase and uppercase
letters = string.ascii_lowercase + string.ascii_uppercase

# letters with only lowercase
# letters = [chr(i) for i in range(97, 123)]

def caesar_cipher(char, shift, operation):
    new = ""
    for let in char:
        if let in letters:
            index = letters.index(let)
            if operation == "encryption":
                new_char = (index + shift) % 26 if let.islower() else (index + shift) % 26 + 26
            elif operation == "decryption":
                new_char = (index - shift) % 26 if let.islower() else (index - shift) % 26 + 26
            new += letters[new_char]
        else:
            new += let
    return new

another = True
while another:
    try:
        shift_value = int(input("Enter a shift value: ")) % 26
        command = int(input("What do you want to do?\n1. Encrypt\n2. Decrypt\n"))
        if command not in [1, 2]:
            raise ValueError("Invalid command. Please enter 1 for Encrypt or 2 or Decrypt.")
        
        operation = "encryption" if command == 1 else "decryption"
        characters = input("Enter what you want to encrypt or decrypt: \n")

        result = caesar_cipher(char=characters, shift=shift_value, operation=operation)

        print(f"The {operation} for {characters} is:\n{result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # ask if the user wants to go again    
    again = int(input("Do you want to go again?\n1. Yes\n2. No\n"))
    if again == 2:
        another = False

