def find_palindrome(user_input):
    reversed_user_input = user_input[::-1]
    
    if user_input == reversed_user_input:
        print("it's a palindrome!")
    
    else:
        print("It's not a palindrome!")


user_input = input("Enter a word: ")

# Formats the user input by transforming into lower case and splits the string.
formatted_user_input = ''.join(user_input.lower().split())

# Any whitespace will be formatted and any numeric input will be handled with a message.
if not user_input.replace(" ", "").isalpha():
        print("Invalid input: please, enter words only.")
        
else:
    find_palindrome(formatted_user_input)