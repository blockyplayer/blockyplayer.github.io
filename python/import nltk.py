

import nltk
from nltk.corpus import words
nltk.download()
# Download the words dataset if you haven't already
nltk.download('words')

# Get the list of English words
word_list = words.words()

# Create a dictionary with unique numbers for each word
word_to_number = {i: word for i, word in enumerate(word_list, start=1)}

# Save the dictionary to a file
with open('word_to_number.json', 'w') as file:
    import json
    json.dump(word_to_number, file)

# Load the dictionary from the file
with open('word_to_number.json', 'r') as file:
    word_to_number = json.load(file)

# Example usage: Get the number for the word "hello"
word = "hello"
number = word_to_number.get(word, "Word not found")
print(f"The number for the word '{word}' is {number}")