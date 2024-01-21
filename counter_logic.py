import os

class WordCounter:

    # Constructor
    def __init__(self, input_text = None):
        self.input_text = input_text

    # Count words in the given text
    def count_words_in_text(self):
        if self.input_text:
            # Split the text into words and return the word count
            words = self.input_text.split()
            return len(words)
        else:
            print("No input provided.")
            return 0

    # Count words in the given file
    def count_words_in_file(self, file_path):
        # If the file exists, read its content, split into words, and return the word count
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                words = content.split()
                return len(words)
        else:
            print(f"File not found: {file_path}")
            return 0