def get_words_of_length(data, length):
    '''Returns a list of words of a given length'''
    words_length = []
    for word in data:
        if len(word) == length:
            words_length.append(word)
    return words_length

def get_words_including(data, string):
    '''Returns a list of words including the string anywhere in the word'''
    words_including = []
    for word in data:
        if string in word:
            words_including.append(word)

    return words_including


def get_words_starting(data, string):
    '''Returns a list of words that include the string at the start of the word'''
    words_starting = []
    for word in data:
        if string == word[:len(string)]:
            words_starting.append(word)
    return words_starting

def get_words_ending(data, string):
    '''Returns a list of words that include the string at the end of the word'''
    words_ending = []
    for word in data:
        starting_index = len(word) - len(string)

        if string == word[starting_index:] :
            words_ending.append(word)
    return words_ending