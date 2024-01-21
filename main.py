from counter_logic import WordCounter

class FormatError(Exception):
    """Custom exception for invalid file format."""

def is_text_file(filename):
    """Check if the file is a .txt file"""
    return filename.lower().endswith('.txt')

def main():
    choice = input("Enter the type of input [text/file]: ").lower()

    if choice == 'text':
        input_text = input("Enter the text: ")
        # Creating a WordCounter object with the provided input_text
        word_counter = WordCounter(input_text)
        word_count = word_counter.count_words()
        print(f"Number of words in the given text: {word_count}")
    elif choice == 'file':
        print("Only text files (.txt) are allowed")
        try:
            file_path = ''
            # Loop until valid file is provided
            while True:
                try:
                    file_path = input("Enter the text file path: ")
                    if is_text_file(file_path):
                        break
                    else:
                        raise FormatError("Invalid input. Please enter a valid text file.")
                except FormatError as e:
                    print(str(e))
            # Open the given file in read mode
            with open(file_path, 'r') as file:
                file_text = file.read()
                # Creating a WordCounter object with the provided input_text
                word_counter = WordCounter(file_text)
                word_count = word_counter.count_words_in_file(file_path)
            print(f"Number of words in the file '{file_path}': {word_count}")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return
    else:
        print("Invalid choice entered.")
        return

if __name__ == "__main__":
    main()