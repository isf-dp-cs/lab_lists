from word_transformations import get_words_of_length, get_words_including, get_words_starting, get_words_ending, get_unique_words


# TODO Use this file to solve the questions in word_exercises.md

file = open("words_100k.txt","r")
words = []
for line in file:
    words.append(line.strip())

