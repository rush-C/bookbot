def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(some_text):
    words = some_text.split()
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = word_counter(book_text)
    print(f"The book contains {word_count} words.")




main()    