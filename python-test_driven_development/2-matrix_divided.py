cat > 2-matrix_divided.py <<'EOF'
#!/usr/bin/python3
"""2-matrix_divided module.

This module provides matrix_divided(matrix, div).
It divides all elements of a matrix by div and rounds to 2 decimals.
No modules are imported.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Returns a new matrix with each element divided by div (rounded to 2 decimals).
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(err_matrix)

    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(err_matrix)
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(err_matrix)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)

    return new_matrix
EOF
