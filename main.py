def main():
    
    book_path = "Book_bot/books/frankenstein.txt"
    text = book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    
    print(f"-- Begin report of {book_path} --")
    print(f"{word_count} words found in the document\n")
    
    for nums in letter_count:
        letter = nums["character"]
        count = nums["nums"]
        
        print(f"The '{letter}' character was found {count} times")
    
    print("--- End report ---")
    
def book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count =  {}
    string = text
    lowered_string = string.lower()
    letters_count_list = []
    
    for letter in lowered_string:
        if letter.isalpha():
            letter_count[letter] = 1 + letter_count.get(letter, 0)

    for letter in letter_count:
        letters_count_list.append({"character" : letter, "nums": letter_count[letter]})
        
    letters_count_list.sort(reverse=True, key=sort_on)
    
    return letters_count_list

def sort_on(dict):
     return dict["nums"]

main()
