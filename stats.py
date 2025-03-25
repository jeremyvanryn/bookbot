def get_book_text(filepath):
    with open(filepath) as f:
        document_text =f.read()
        #print(document_text)
    return document_text

def count_words(document_string):
    list_of_words = document_string.split()
    num_words = len(list_of_words)
    print(f"{num_words} words found in the document")

def count_character(document_string):
    document_lower = document_string.lower()
    #use a dictionary string>integer
    # establish the dictionary
    dictionary = {}

    for a in document_lower:
        #if the key isnt established
        if a not in dictionary:
            var_name = a
            var_count = 1
            dictionary[var_name] = var_count
        #if the key is established
        else:
            dictionary[a] += 1
    return print(dictionary)