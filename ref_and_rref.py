def print_matrix(matrix):
    for row in matrix:
        print(row)

def perform_ref(matrix):
    m, n = len(matrix), len(matrix[0])

    for i in range(min(m, n)):
        # Make the diagonal element 1
        pivot = matrix[i][i]
        if pivot == 0:
            # If the pivot is 0, swap rows with a non-zero pivot
            for j in range(i + 1, m):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
            else:
                raise ValueError("Matrix is singular; cannot perform REF")

            pivot = matrix[i][i]

        # Normalize the row
        matrix[i] = [elem / pivot for elem in matrix[i]]

        # Eliminate other elements in the column
        for j in range(i + 1, m):
            factor = matrix[j][i]
            matrix[j] = [elem - factor * matrix[i][k] for k, elem in enumerate(matrix[j])]

def perform_rref(matrix):
    m, n = len(matrix), len(matrix[0])

    perform_ref(matrix)

    # Back-substitution to make upper triangular matrix
    for i in range(min(m, n) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            factor = matrix[j][i]
            matrix[j] = [elem - factor * matrix[i][k] for k, elem in enumerate(matrix[j])]

def main():
    # Example input matrix A and vector b
    A = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ]
    b = [8, -11, -3]

    # Construct augmented matrix
    augmented_matrix = [row + [bi] for row, bi in zip(A, b)]

    print("Augmented Matrix:")
    print_matrix(augmented_matrix)

    # Perform REF
    perform_ref(augmented_matrix)
    print("\nRow Echelon Form (REF):")
    print_matrix(augmented_matrix)

    # Perform RREF
    perform_rref(augmented_matrix)
    print("\nReduced Row Echelon Form (RREF):")
    print_matrix(augmented_matrix)

if __name__ == "__main__":
    main()
