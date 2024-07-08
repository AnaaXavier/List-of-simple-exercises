def find_even_or_odd(user_input):
    if user_input % 2 == 0:
        return "It's an even!"
    else:
        return "It's an odd!"

user_input = int(input("Enter a number: "))
result = find_even_or_odd(user_input)

print(result)