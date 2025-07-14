def calculate_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return abs(determinant)
    else:
        # Laplace expansion
        det = 0
        for i in range(len(matrix)):
            minor = get_minor(matrix, 0, i)  # Corrected function call
            cofactor = (-1) ** i * matrix[0][i] * calculate_determinant(minor)  # Corrected recursive call
            det += cofactor
        return det

def get_minor(matrix, row, col):
    return [r[:col] + r[col + 1:] for r in (matrix[:row] + matrix[row + 1:])]

# Test matrices
# one_by_one = [[1]]
# two_by_two = [[1, 2], [3, 4]]
# three_by_three = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# four_by_four = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# # Calculate the determinant of the matrices
# print(f"1x1: {calculate_determinant(one_by_one)}")  # 1
# print(f"2x2: {calculate_determinant(two_by_two)}")  # -2
# print(f"3x3: {calculate_determinant(three_by_three)}")  # 0
# print(f"4x4: {calculate_determinant(four_by_four)}")  # 0