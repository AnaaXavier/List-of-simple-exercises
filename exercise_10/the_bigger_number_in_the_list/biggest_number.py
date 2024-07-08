list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

max_number = list_of_numbers[0]

for current_number in list_of_numbers[1:]:
    if current_number > max_number:
        max_number = current_number

print(f"The biggest number in the list is: {max_number}")
