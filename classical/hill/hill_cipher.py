import math
import numpy as np
from det import get_minor, calculate_determinant

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
        if let.isalpha():
            cleaned_message.append(let)
    return cleaned_message

def key_management(key):
    key_matrix = []
    key_numeric = []

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
            key_numeric.append(alphabet_to_number['X'])

    # getting the key matrix
    matrix_size = int(math.sqrt(len(key_numeric)))
    for row in range(0, len(key_numeric), matrix_size):
        key_matrix.append(key_numeric[row:row + matrix_size])
    
    return matrix_size, key_matrix

def closest_multiple(message, key):
    message_length = len(message)

    if message_length % matrix_size == 0:
        return 0
    
    key_length =  len(key)
    matrix_size = int(math.sqrt(key_length))

    if message_length % matrix_size == 0:
        return 
    else:
        upper_bound = (message_length // matrix_size + 1) * matrix_size
        return upper_bound - message_length
    
def mod_inverse(determinant, mod=26):
    determinant = determinant % mod
    for x in range(1, mod):
        if (determinant * x) % mod == 1:
            return x
    return None

def adjugate_matrix(matrix):
    size = len(matrix)
    cofactor_matrix = []

    for i in range(size):
        row = []
        for j in range(size):
            minor = get_minor(matrix, i, j)
            minor_det = calculate_determinant(minor) % 26
            cofactor = (-1) ** (i + j) * minor_det
            row.append(cofactor)
        cofactor_matrix.append(row)

    adjugate = np.array(cofactor_matrix).T.tolist()
    return adjugate

def inverse_matrix_mod26(matrix):
    det_A = calculate_determinant(matrix) % 26
    if det_A < 0:
        det_A += 26
    mod_inv = mod_inverse(det_A, 26)

    if mod_inv is None:
        raise ValueError("Matrix is not invertible")
    
    adjugate_A = adjugate_matrix(matrix)
    inverse_mod26 = [[(mod_inv * adjugate_A[i][j]) % 26 for j in range(len(matrix))] for i in range(len(matrix))]

    return inverse_mod26



def cipherFunct(key, plaintext, action):
    cipher = []
    plaintext_matrix = []
    plaintext_numeric = []
    key_matrix = []

    clean_text = handle_text(plaintext=plaintext)
    multiple = closest_multiple(message=clean_text, key=key)

    if multiple:
        for _ in range(multiple):
            clean_text.append("X")

    for let in clean_text:
        plaintext_numeric.append(alphabet_to_number[let])

    matrix_size, key_matrix = key_management(key=key)

    if action == "encryption":
        for row in range(0, len(plaintext_numeric), matrix_size):
            plaintext_matrix.append(plaintext_numeric[row:row + matrix_size])

        for num in range(len(plaintext_matrix)):
            plain_row = plaintext_matrix[num]
            for j in range(len(key_matrix)):
                result = sum(plain_row[k] * key_matrix[j][k] for k in range(len(key_matrix[j])))
                cipher.append(result % 26)
    elif action == "decryption":
        key_matrix = inverse_matrix_mod26(key_matrix)

        for row in range(0, len(plaintext_numeric), matrix_size):
            plaintext_matrix.append(plaintext_numeric[row:row + matrix_size])

        for num in range(len(plaintext_matrix)):
            plain_row = plaintext_matrix[num]
            for j in range(len(key_matrix)):
                result = sum(plain_row[k] * key_matrix[j][k] for k in range(len(key_matrix[j])))
                cipher.append(result % 26)
    else:
        print("Invalid action")

    cipher_text = [number_to_alphabet[num] for num in cipher]
    return "".join(cipher_text)


key = "HILLCIPHER"
plaintext = "Learning about Crypto"
encrypt = cipherFunct(key=key, plaintext=plaintext, action="encryption")
print(f"The encrypted message for {plaintext}: {encrypt}\n")
decrypt = cipherFunct(key=key, plaintext=encrypt, action="decryption")
print(f"The decrypted message for {encrypt}: {decrypt}\n")




