def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def letter_count(book_text):
    count = {}

    for character in book_text.lower():
        count[character] = count.get(character, 0) + 1

    return count

def sort_letter_count(letter_counts):
    to_sort = {k: v for k, v in letter_counts.items() if k.isalpha()}
    return sorted(to_sort.items(), key=lambda item: item[1], reverse=True)