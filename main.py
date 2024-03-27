def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_count = get_char_count(text.lower())

def get_char_count(text):
    ...


def get_num_words(text):
    return len(text.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()