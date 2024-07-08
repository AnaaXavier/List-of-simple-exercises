def transform_list_to_matrix(a_list, rows, cols):
    matrix = []
    for i in range(rows):
        matrix_rows = []
        for j in range(cols):
            matrix_rows.append(a_list[i* cols + j])
        matrix.append(matrix_rows)
        
    return matrix

rows = 2
cols = 3

a_list = [1, 2, 3, 4, 5, 6]

result = transform_list_to_matrix(a_list, rows, cols)

for rows in result:
    print(rows)