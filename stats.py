def word_count(filepath):

    word_count = 0
    output = get_book_text(filepath)

    for words in output.split():
            word_count += 1
    return word_count

def get_book_text(filepath):

    with open(filepath) as f: 
        file_contents = f.read()
    return file_contents

def character_count(filepath):
     
     characters = {}
     output = get_book_text(filepath)
     
     for char in output.lower():
            if char not in characters:
                    characters[char] = 1
            else:
                 characters[char] += 1
     return characters

def sorted_char_count(filepath):
      
      output_of_charcount = character_count(filepath)
      two_key_count = []

      for char in output_of_charcount:
            if char.isalpha():
                  two_key_count.append({"char": char, "count":output_of_charcount[char]})
        
      two_key_count.sort(key=lambda item: item["count"], reverse=True)

      return two_key_count