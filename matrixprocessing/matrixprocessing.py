"""Matrix-processing project:The program implements various operations with matrices"""
import random
import copy

# DICTIONARY FOR WORKING WITH THE PROGRAM MENU
menu_options = {
    1: 'Add matrices',
    2: 'Multiply matrix by a constant',
    3: 'Multiply matrices',
    4: 'Transpose matrix',
    5: 'Calculate a determinant',
    6: 'Inverse matrix',
    0: 'Exit',
}


def print_menu():
    """GAP FILLING WITH SYMBOLS"""
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def show_one_matrix():
    """OUTPUT OF ONE MATRIX WITH RANDOM VALUES"""
    """
       Returns:
       -------
               matrix_a (int): int.
       -------
    """
    while True:
        try:
            length_a = int(input("Enter the length of the matrix A ->"))
            height_a = int(input("Enter the height of the matrix A ->"))
            matrix_a = [[random.randint(-50, 50) for _ in range(length_a)] for _ in range(height_a)]
            print(*matrix_a, sep='\n')

            return matrix_a
        except ValueError:
            print("Enter only numbers!")


# noinspection PyBroadException
def show_two_matrix():
    """OUTPUT OF TWO MATRIXES WITH RANDOM VALUES"""
    """
       Returns:
       -------
               matrix_a (int): int;
               matrix_b (int): int.
       -------
     """
    while True:
        try:
            length_a = int(input("Enter the length of the matrix A ->"))
            height_a = int(input("Enter the height of the matrix A ->"))
            matrix_a = [[random.randint(-50, 50) for _ in range(length_a)] for _ in range(height_a)]
            print(*matrix_a, sep='\n')
            length_b = int(input("Enter the length of the matrix B ->"))
            height_b = int(input("Enter the height of the matrix B ->"))
            matrix_b = [[random.randint(-50, 50) for _ in range(length_b)] for _ in range(height_b)]
            print(*matrix_b, sep='\n')
            return matrix_a, matrix_b
        except:
            print("Enter only numbers!")


def add_matrices():
    """ADDING AND ADDING TWO MATRIXES"""
    print('\'Add matrices\'')
    matrix_a, matrix_b = show_two_matrix()
    # noinspection PyBroadException
    try:
        result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
        print("RESULT")
        for r in result:
            print(r)
    except ValueError:
        print("ERROR")


def multiply_by_constant():
    """ADDING AND MULTIPLYING A MATRIX BY A CONSTANT"""
    matrix_a = show_one_matrix()
    matrix_const = (input("Enter constant - >"))
    try:
        result = [[matrix_a[i][j] * float(matrix_const) for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
        print("RESULT")
        for r in result:
            print(r)
    except ValueError:
        print("ERROR!Enter only numbers")


def multiply_matrices():
    """ADDING AND MULTIPLYING TWO MATRIXES"""
    matrix_a, matrix_b = show_two_matrix()
    print('\'Multiply matrices\'')
    # noinspection PyBroadException
    try:
        result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*matrix_b)] for X_row in matrix_a]
        print("RESULT")
        for r in result:
            print(r)
    except ValueError:
        print("ERROR")


def transpose_matrix():
    """ADD AND TRANSPOSE A SINGLE MATRIX"""
    matrix_a = show_one_matrix()
    zip_matrix = zip(*matrix_a)
    print("TRANSPOSE")
    for row in zip_matrix:
        print(row)


def calculate_determinant():
    """ADDING A MATRIX AND ASSIGNING VALUES"""
    matrix_a = show_one_matrix()
    a_length = len(matrix_a[0])
    a_height = len(matrix_a)
    if a_height == a_length:
        def calc(n, matrix):
            """CALCULATION OF THE DETERMINANT"""
            if n == 2:
                d = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
                return d
            else:
                d = int(0)
                temp = copy.deepcopy(matrix)
                line = copy.deepcopy(temp[0])
                temp.pop(0)
                for j in range(0, n):
                    temp2 = copy.deepcopy(temp)
                    for k in range(0, n - 1):
                        temp2[k].pop(j)
                    d += ((-1) ** (0 + j + 2)) * line[j] * (calc(n - 1, temp2))
                return d
        # OUTPUT RESULT
        for i in matrix_a:
            print(' '.join(map(str, i)))
        print(f'Your determinant:  {str(calc(a_length, matrix_a))}')
    else:
        print("ERROR")


def inverse_matrix():
    """ADDITION AND DEFINITION OF THE INVERSE MATRIX"""
    """
    For non-square matrices and degenerate matrices there are no inverse matrices
    Matrix must be square (i.e. have the same number of rows as columns)
       Returns:
       -------
               double_l (int): int;
               m (int): int.
       -------
    """
    matrix_a = show_one_matrix()
    a_length = len(matrix_a[0])
    a_height = len(matrix_a)
    if a_height == a_length:
        def gen_id_mat(n):
            """Convert the element on the main diagonal to 1."""
            double_l = [[0 for _ in range(n)] for _ in range(n)]
            for k in range(n):
                double_l[k][k] = 1
            return double_l

        def gen_id_mat1(n):
            """Convert the element on the main diagonal to 1."""
            double_l = [[0.0 for _ in range(n)] for _ in range(n)]
            for k in range(n):
                double_l[k][k] = 1.0
            return double_l

        def row_swap(m, r1, r2):
            """Swap rows if m=0. This step is necessary for exceptional situations of being on the main diagonal 0."""
            m[r1], m[r2] = m[r2], m[r1]
            return m

        def row_op_1(m, r1, r2, c):
            """permutation of strings, multiplication of a string by a constant"""
            for i in range(len(m)):
                m[r1][i] = (m[r2][i]) * c
            return m

        def row_op_2(m, r1, r2, c):
            """permutation of strings, multiplication of a string by a constant"""
            for i in range(len(m)):
                m[r1][i] = m[r1][i] - (c * m[r2][i])
            return m

        def disp(m):
            print('\n'.join([' '.join(['{:4}'.format(item) for item in x]) for x in m]))
            pass

        idm = gen_id_mat(a_height)
        id_inv = gen_id_mat(a_height)

        count = 0
        # CHECKING THE DETERMINANT IS NOT ZERO
        for col in range(a_height):
            for row in range(a_height):
                if idm[row][col] == 1 and matrix_a[row][col] == 0:
                    for g in range(a_height):
                        if matrix_a[g][col] != 0:
                            matrix_a = row_swap(matrix_a, row, g)

                if matrix_a[row][col] != 0 and idm[row][col] == 1:
                    # multiply = 1 / matrix[row][col]
                    id_inv = row_op_1(id_inv, row, row, (1 / matrix_a[row][col]))
                    matrix_A = row_op_1(matrix_a, row, row, (1 / matrix_a[row][col]))
                    count += 1
                    for const in range(a_height):
                        if const == row:
                            continue
                        # multiply = matrix[const][col]
                        id_inv = row_op_2(id_inv, const, row, matrix_a[const][col])
                        matrix_A = row_op_2(matrix_A, const, row, matrix_a[const][col])

                        count += 1
        # OUTPUT RESULT
        if matrix_a == gen_id_mat1(a_height):
            print("Your matrix:")
            print()
            disp(id_inv)
        else:
            print("This matrix cant be inverse")
            inverse_matrix()
    else:
        print("ERROR")


# APP MENU
if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except option:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            add_matrices()
        elif option == 2:
            multiply_by_constant()
        elif option == 3:
            multiply_matrices()
        elif option == 4:
            transpose_matrix()
        elif option == 5:
            calculate_determinant()
        elif option == 6:
            inverse_matrix()
        elif option == 0:
            print('Bye!')
            exit()
        else:
            print('Invalid option. Please enter a number between 0 and 6.')
