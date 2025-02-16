from string import ascii_lowercase


def char_counter(some_text):
    arr_dict = []
    all_chars = []
    some_text = some_text.lower()
    for char in some_text:
        if char not in all_chars:
            all_chars.append(char)

    for char in all_chars:
        if char in ascii_lowercase:
            arr_dict.append({"char" : char, "num" : some_text.count(char)})  

    return arr_dict




def sort_on(dict):
    return dict["num"]

def max_to_min(arr):
    arr.sort(reverse=True, key=sort_on)
    return arr


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
    print(f"--- Begin report of {book_path} ---")
    print(f"The book contains {word_count} words.\n")
    char_list = char_counter(book_text)         # contains chars and occurences of each char in num for each in array
    char_list = max_to_min(char_list)
    for item in char_list:
        print(f"The {item["char"]} character was found {item["num"]} times")

    print("--- End report ---")


main()    