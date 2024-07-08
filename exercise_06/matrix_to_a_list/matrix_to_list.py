def transform_matrix_to_list(a_matrix):
    one_dimension_list = [an_element for line in a_matrix for an_element in line]
    return one_dimension_list

a_matrix = [[2, 4, 6],
            [8, 10, 12]]

result = transform_matrix_to_list(a_matrix)
print(result)