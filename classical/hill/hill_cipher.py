import math

def is_perfect_square(num):
    if num < 0:
        return False
    sqrt = math.isqrt(num)
    return sqrt * sqrt ==  num

def handle_text(plaintext):
    text_upper = plaintext.upper()
    text = text_upper.replace(" ", "")
    cleaned_message = []

    for let in text:
        if let.isalpha:
            cleaned_message.append(let)
    return cleaned_message

def key_management(key):
    # convert letters in the key to numbers
    for letter in key:
        key_numeric.append(alphabet_to_number[letter])

    # if key length is not a perfect square 
    if not is_perfect_square(len(key_numeric)):
        if is_perfect_square(len(key_numeric) - 1):
            # if the number before the key length is a perfect square, remove from the list
            key_numeric.pop()
        elif is_perfect_square(len(key_numeric) + 1):
            # if the number afte the key length is a perfect square, add an 'X'
            key_numeric.append('X')

    # getting the key matrix
    matrix_size = int(math.sqrt(len(key_numeric)))
    for row in range(0, len(key_numeric), matrix_size):
        key_matrix.append(key_numeric[row:row + matrix_size])
    
    return matrix_size, key_matrix

def closest_multiple(message, key):
    message_length = len(message)
    key_length =  len(key)
    matrix_size = int(math.sqrt(key_length))

    if message_length % matrix_size == 0:
        return 
    else:
        upper_bound = (message_length // matrix_size + 1) * matrix_size
        return upper_bound - message_length
    
def encryption(key, plaintext):
    clean_text = handle_text(plaintext=plaintext)
    multiple = closest_multiple(message=clean_text, key=key)

    if multiple:
        for _ in range(multiple):
            clean_text.append("X")

    for let in clean_text:
        plaintext_numeric.append(alphabet_to_number[let])

    matrix_size, key_matrix = key_management(key=key)
    for row in range(0, len(plaintext_numeric), matrix_size):
        plaintext_matrix.append(plaintext_numeric[row:row + matrix_size])

    for num in range(len(plaintext_matrix)):
        plain_row = plaintext_matrix[num]
        for j in range(len(key_matrix)):
            result = []
            key_row = key_matrix[j]
            for val in range(len(key_row)):
                value = (plain_row[val] * key_row[val])
                result.append(value)
            final = sum(result) % 26
            cipher.append(final)

    cipher_text = [number_to_alphabet[num] for num in cipher]
    return "".join(cipher_text)

alphabet_to_number = {chr(i): i - ord('A') for i in range(ord('A'), ord('Z') + 1)}
number_to_alphabet = {value: key for key, value in alphabet_to_number.items()}

# key management storages
key_matrix = []
key_numeric = []
matrix_size = []

# encryption decryption storages
plaintext_numeric = []
plaintext_matrix = []
cipher = []

key = "HILLCIPHER"
plaintext = "Learning about Crypto"
encrypt = encryption(key=key, plaintext=plaintext)
print(f"The encrypted message for {plaintext}: {encrypt}")




