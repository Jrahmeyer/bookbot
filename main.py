from stats import get_num_words, get_num_chars, sort_on
import sys

def get_book_text(f):
    return f

def main():
    if len(sys.argv) > 1:
        first_arg = sys.argv[1]
        with open(f"{first_arg}") as f:
            file_contents = f.read()
            #print(get_book_text(file_contents))
            #print(f"{get_num_words(file_contents)} words found in the document")
            #print(get_num_chars(file_contents))
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {first_arg}. . .")
            print("----------- Word Count ----------")
            print(f"Found {get_num_words(file_contents)} total words")
            print("--------- Character Count -------")
            for line in sort_on(get_num_chars(file_contents)):
                print(line)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
