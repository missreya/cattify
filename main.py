import catpuns

def replace_words(sentence:str, synonyms:str):
    '''Replaces complete full words with cattified words dictionary'''
    
    cat_sentence = sentence

    if synonyms == "" or synonyms.upper()[0] == 'Y':
        for key, value in catpuns.synonym_dict.items():
            cat_sentence = cat_sentence.replace(key, value)

    for key, value in catpuns.word_dict.items():
        cat_sentence = cat_sentence.replace(key, value)

    for key, value in catpuns.syllable_dict.items():
        cat_sentence = cat_sentence.replace(key, value)

    if sentence != cat_sentence:
        cat_sentence = cat_sentence + " :3"

    return cat_sentence


phrase = input('Enter a sentence: ')
synonyms = input("Would you like some words replaced with synonyms for maximum catification? Enter Y to be a cool cat: ")
print(replace_words(phrase, synonyms))