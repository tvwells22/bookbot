def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_count(text)
    sorted_list = sorted_characters(char_dict)
    print_report(book_path, num_words, sorted_list)
   
def print_report(book_path, num_words, sorted_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    print(f"{sorted_list}\n --- End report ---")


def sort_on(dict):
    return dict["character"]
    

def sorted_characters(char_dict):
    #Convert the dictionary into a list of dictionaries
    char_list = []
    for key in char_dict:
        char_list.append({"character" : key, "count" : char_dict[key]})
    #Create a new list that is only the letters
    letter_list = []
    for dict in char_list:
        if dict["character"].isalpha():
            letter_list.append(dict)
    #Sort the new list into alphabetical order
    letter_list.sort(reverse=False, key=sort_on)
    
    return letter_list


def get_char_count(text):
    chars = {}
    for letter in text.lower():
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    return chars


def get_num_words(text):
    return len(text.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()