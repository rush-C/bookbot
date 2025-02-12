def char_counter(some_text):
    dict = {}
    all_chars = []
    some_text = some_text.lower()
    for char in some_text:
        if char not in all_chars:
            all_chars.append(char)

    for char in all_chars:
        dict[char] = some_text.count(char)        

        
    return(dict)


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
    dictionary = char_counter(book_text)
    print(dictionary)




main()    