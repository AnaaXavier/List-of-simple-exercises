import re

user_text = input("Enter a phrase: ")
pattern = r'[Aa]' # The pattern finds the letter "A", it's case insensitive.

pattern_in_text = re.findall(pattern, user_text)
count_letter = len(pattern_in_text)

print(f"The letter 'a' repeated {count_letter} times in the phrase!")