def square_matrix_simple(matrix=[]):
    new_matrix = []
    for line in matrix:
        new_line = []
        for value in line:
            new_line.append(value ** 2)
        new_matrix.append(new_line)
    return new_matrix
