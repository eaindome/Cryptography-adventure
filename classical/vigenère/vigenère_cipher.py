import string

# letters with now both lowercase and uppercase
letters = string.ascii_lowercase + string.ascii_uppercase

# starting with only lowercase
# letters = [chr(i) for i in range(97, 123)]

def generate_key(text, keyword):
    # remove non-alphabetic characters
    filtered_text = "".join([char for char in text if char.isalpha()])
    key = keyword
    while len(key) < len(filtered_text):
        key += keyword
    return key[:len(filtered_text)]
    
def vigenère_cipher(text, key, operation):
    newChar = ""
    key_index = 0       # for tracking the key index
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

another = True
while another:
    try:
        text = input("Enter your text:\n")
        keyword = input("Enter your keyword:\n")
        key = generate_key(text=text, keyword=keyword)

        command = int(input("What do you want to do?\n1. Encrypt\n2. Decrypt\n"))
        if command not in [1, 2]:
            raise ValueError("Invalid command. Please enter 1 for Encrypt or 2 or Decrypt.")
        
        operation = "encryption" if command == 1 else "decryption"

        result = vigenère_cipher(text=text, key=key, operation=operation)

        print(f"The {operation} for {text} is:\n{result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # ask if the user wants to go again    
    again = int(input("Do you want to go again?\n1. Yes\n2. No\n"))
    if again == 2:
        another = False

# for testing purposes
# text = "GEEKSFORGEEKSgh"
# keyword = "AYUsh"
# key = generate_key(text=text, keyword=keyword)

# if operation == "encryption":
#                 index = (letters.index(text[i]) + letters.index(key[i])) % 26 if text[i].islower() else (letters.index(text[i]) + letters.index(key[i])) % 26 + 26
#             elif operation == "decryption":
#                 index = (letters.index(text[i]) - letters.index(key[i]) + 26) % 26 if text[i].islower() else (letters.index(text[i]) - letters.index(key[i]) + 26) % 26 + 26
#         newChar += letters[index]