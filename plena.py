def find_first_non_repeated(word):
    """
    Case is not considered in whether a letter is repeated
    Repetition is defined as any letter that occurs two or more times in sequence
    Return the first non-repeated letter in a string."""
    if len(word) > 0:
        first = word[0].lower()
        duplicate = False
        for i in range(1,len(word)):
            if first == word[i].lower():
                duplicate = True
                continue
            else:
                if duplicate:
                    first = word[i].lower()
                    duplicate = False
                else:
                    return first
        return first
    else:
        return ''

def remove_duplicates(word):
    """
    remove repeated letters from a word"""
    letters = []
    for i in word:
        if i.lower() in letters:
            continue
        else:
            letters.append(i.lower())           
    return letters
        
def get_letters(word):
    """
    Takes a word as input and returns a dictionary containing a key of the lowercase letter
    and a value containing an ordered list of all occurances of that letter"""
    letter_dict = {}
    for i in word:
        if i.lower() not in letter_dict:
            letter_dict[i.lower()] = list(i)
        else:
            letter_dict[i.lower()].append(i)
    return letter_dict

def create_letter_order(letters,letter_dict):
    """
    Rearrange the word so that it appears in order of appearance and frequency"""   
    new_word = [letter_dict[l] for l in letters]
    counts = [len(i) for i in new_word]
    indices = sorted(range(len(counts)), key=lambda k: counts[k])

    new_word = [new_word[i] for i in indices]
    new_word = ''.join([i for j in new_word for i in j])
    return new_word    
            

word = input("Enter a Word: ")
print(find_first_non_repeated(word))
print(create_letter_order(remove_duplicates(word), get_letters(word)))
    
            