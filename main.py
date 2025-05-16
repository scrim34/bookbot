from stats import word_count, character_count, sorted_char_count
import sys

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) >= 1:
        filepath = sys.argv[1]
    
    words = word_count(filepath)
    characters = character_count(filepath)
    sorted = sorted_char_count(filepath)
          
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        print(f"{item['char']}: {item['count']}")
    print("============= END ==============")


main()
