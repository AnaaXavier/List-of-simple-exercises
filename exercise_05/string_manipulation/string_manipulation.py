# the phrase that'll be used for string manipulation
phrase_example = "Hello world!"

# inverting
inverted_phrase = phrase_example[::-1]

print("Inverted: ", inverted_phrase, end="\n\n")

# slicing
sliced_phrase = phrase_example[:8]
another_sliced_phrase = phrase_example[:-1]

print("First example of slicing: ", sliced_phrase, end="\n\n")
print("Second example of slicing: ", another_sliced_phrase, end="\n\n")

# concatenation
first_part = "Hello "
second_part = "world"

result = first_part + second_part + "!"

print("Concatenated: ", result, end="\n\n")

# splitting
splitting = phrase_example.split("!")

print("Splitting: ", splitting, end="\n\n")

# Case conversion

all_phrase_in_uppercase = phrase_example.upper()

print("Uppercase: ", all_phrase_in_uppercase, end="\n\n")

all_phrase_in_lower = phrase_example.lower()

print("Lowercase: ", all_phrase_in_lower, end="\n\n")

phrase_with_uppercase = phrase_example[0:5] + " " + phrase_example[6:9].upper() + phrase_example[9:12]

print("Uppercase in some letters: ", phrase_with_uppercase, end="\n\n")

# or we can do like this

modified_chars = []

for characters in range(len(phrase_example)):
    if characters in [4, 6, 7, 8]:
        modified_chars.append(phrase_example[characters].upper())  # Convert to uppercase if true
    else:
        modified_chars.append(phrase_example[characters])

phrase_using_join_uppercase = ''.join(modified_chars)

print("Another example of uppercase in some letters: ", phrase_using_join_uppercase, end="\n\n")

# Stripping

another_phrase_example = "---------HELLO WORLD!-----"
stripped_phrase_example = another_phrase_example.strip("-")

print("Stripping: ", stripped_phrase_example, end="\n\n")