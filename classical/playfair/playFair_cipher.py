def remove_duplicates(key):
    seen = set()
    result = []
    for char in key:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)

def create_playfair_grid(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = remove_duplicates(key=keyword)
    key = key.upper()

    # combine the keyword with the alphabet
    combined_key = key + alphabet

    # check if there are duplicates in the combined key
    combined_key = remove_duplicates(combined_key)

    # create the playfair grid
    playfair_grid = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(combined_key[i * 5 + j])
        playfair_grid.append(row)

    # find the letter positions
    letter_positions = {}
    for row in range(5):
        for col in range(5):
            letter_positions[playfair_grid[row][col]] = (row, col)
    return playfair_grid, letter_positions

def separate_text(plaintext):
    # clean the plaintext
    plaintext = plaintext.upper()
    plaintext = plaintext.replace("J", "I")
    plaintext = plaintext.replace(" ", "")
    cleaned_message = ""

    for let in plaintext:
        if let.isalpha():
            cleaned_message += let

    # separate the plaintext into pairs
    pairs = []
    i = 0

    while i < len(cleaned_message):
        # first letter
        first_letter = cleaned_message[i]

        if i + 1 < len(cleaned_message):
            second_letter = cleaned_message[i + 1]

            if first_letter == second_letter:
                pairs.append(first_letter + "X")
                i += 1 # move one step forward
            else:
                pairs.append(first_letter + second_letter)
                i += 2 # move two steps forward
        else:
            # if only one letter is left
            pairs.append(first_letter + "X")
            i += 2

    return pairs

def encrypt_pair(pair, letter_positions, grid):
    # deconstruct the pair
    a, b = pair

    # find the positions of the letters
    row_a, col_a = letter_positions[a]
    row_b, col_b = letter_positions[b]

    # Rule 1: if the letters are in the same row
    if row_a == row_b:
        encrypt_a = grid[row_a][(col_a + 1) % 5]
        encrypt_b = grid[row_b][(col_b + 1) % 5]

    # Rule 2: if the letters are in the same column
    elif col_a == col_b:
        encrypt_a = grid[(row_a + 1) % 5][col_a]
        encrypt_b = grid[(row_b + 1) % 5][col_b]

    # Rule 3: if the letters form a rectangle
    else:
        encrypt_a = grid[row_a][col_b]
        encrypt_b = grid[row_b][col_a]

    return encrypt_a + encrypt_b

def decrypt_pair(pair, letter_positions, grid):
    # deconstruct the pair
    a, b = pair

    # find the positions of the letters
    row_a, col_a = letter_positions[a]
    row_b, col_b = letter_positions[b]

    # Rule 1: if the letters are in the same row
    if row_a == row_b:
        decrypt_a = grid[row_a][(col_a - 1) % 5]
        decrypt_b = grid[row_b][(col_b - 1) % 5]

    # Rule 2: if the letters are in the same column
    elif col_a == col_b:
        decrypt_a = grid[(row_a - 1) % 5][col_a]
        decrypt_b = grid[(row_b - 1) % 5][col_b]

    # Rule 3: if the letters form a rectangle
    else:
        decrypt_a = grid[row_a][col_b]
        decrypt_b = grid[row_b][col_a]

    return decrypt_a + decrypt_b

keyword = "PLAYFAIR"
plaintext = "instruments"
ciphertext = "EUTNIVEGONXY"


encrypt_pairs = separate_text(plaintext)
print(f"pairs: {encrypt_pairs}\n")

grid, positions = create_playfair_grid(keyword)
print(f"grid: {grid}\n\npositions: {positions}\n")

encrypted_pairs = []
for pairs in encrypt_pairs:
    encrypted_pairs.append(encrypt_pair(pairs, positions, grid))

print(f"encrypted_pairs: {encrypted_pairs}")
print(f"encrypted message: {"".join(encrypted_pairs)}\n")

decrypt_pairs = separate_text(ciphertext)

decrypted_pairs = []
for pairs in decrypt_pairs:
    decrypted_pairs.append(decrypt_pair(pairs, positions, grid))

# remove any 'X' characters
decrypted_pairs = [pair.replace("X", "") for pair in decrypted_pairs]

print(f"decrypted_pairs: {decrypted_pairs}")
print(f"decrypted message: {"".join(decrypted_pairs)}")