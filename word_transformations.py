# word_transformations.py

def get_word_list(file):
    """Returns a list of words without the newline charachter"""

    file = open(file,'r')
    word_list = []
    for line in file:
        word_list.append(line.strip())
    file.close()
    return word_list

def get_words_of_length(word_list, length):
    '''Returns a list of words of a given length'''
    words = []
    for word in word_list:
        if len(word) == length:
            words.append(word)
    return words

def get_words_including(word_list, including_string):
    '''Returns a list of words including the string anywhere in the word'''
    words = []
    for word in word_list:
        if including_string in word:
            words.append(word)
    return words


def get_words_starting(word_list, starting_string):
    '''Returns a list of words that include the string at the start of the word'''
    words = []
    for word in word_list:
        if starting_string == word[0:len(starting_string)]:
            words.append(word)
    return words

def get_words_ending(word_list, ending_string):
    '''Returns a list of words that include the string at the end of the word'''
    words = []
    for word in word_list:
        length = len(word)
        start = length - len(ending_string)
        if ending_string == word[start:]:
            words.append(word)
    return words


if __name__ == '__main__':

    word_list = get_word_list("words_100k.txt")

    # TODO 1) What is the distrubtion of number of words for all lengths of words in the list? 
    print("\n--TODO 1")

    for i in range(19):
        print(i, len(get_words_of_length(word_list,i)))


    # TODO 2) What is the longest word?
    print("\n--TODO 2")
    print(get_words_of_length(word_list,18))


    # TODO 3) Which words contain the word "ability"? 
    print("\n--TODO 3")
    print(get_words_including(word_list,'ability'))


    # TODO 4) Which 10 letter words contain the word "cat" in them?
    print("\n--TODO 4")
    print(get_words_of_length(get_words_including(word_list,'cat'),10))

    # TODO 5) Which words contain double 'o's and double 's's. 
    print("\n--TODO 5")
    print(get_words_including(get_words_including(word_list,'oo'),'ss'))


    print("\n--TODO 6")
    # TODO 5) Which words have all five vowels (aeiou)?
    print(get_words_including(get_words_including(get_words_including(get_words_including(get_words_including(word_list,'a'),'e'),'i'),'o'),'u'))