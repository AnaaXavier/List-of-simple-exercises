original_phrase = "Hello world!"
# The list compreehension is used to iterate over each character in the original phrase and joining in an empty string
# Also, characters that are not whitespace are replaced by "*". 
censored_phrase = "".join('*' if character != ' ' else ' ' for character in original_phrase)

print(f"Original phrase: {original_phrase}")
print(f"Censored phrase: {censored_phrase}")
