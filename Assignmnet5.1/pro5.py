# Function to check if a word is palindrome.
def is_palindrom(word):
    word = word.lower()
    return word == word[::-1]
print(is_palindrom("madam"))
print(is_palindrom("meet"))