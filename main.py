import sys
from stats import get_num_words as get_num_words
from stats import letter_count as letter_count
from stats import sort_letter_count as sort_letter_count

def get_book_text(filename):
   with open(filename, 'r', encoding='utf-8') as file:
       return file.read()

def main():
    if len(sys.argv) > 1:
        book_file = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(book_file)
    word_count = get_num_words(book_text)
    letter_counts = letter_count(book_text)
    sorted_letter_counts = sort_letter_count(letter_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {book_file}...")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter, count in sorted_letter_counts:
        print(f"{letter}: {count}")
    print("============= END ===============")

main()