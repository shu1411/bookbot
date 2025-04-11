from stats import count_words, count_chars, sort_result
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    content = get_book_text(filepath)
    num_words = count_words(content)
    letter_stats = count_chars(content)
    result = sort_result(letter_stats)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for pair in result:
        print(f"{pair['char']}: {pair['num']}")

    print("============= END ===============")


main()