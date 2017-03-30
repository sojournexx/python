#Andrew Tan, 3/30, Section 010, Part 3a

import random

def add_letters(word, num):
    new_word = ""
    for char in word:
        insert = ""
        for i in range(num):
            rdm = 91
            while rdm in range(91, 97):
                rdm = random.randint(65, 122)
            insert = insert + chr(rdm)
        new_word = new_word + char + insert
    return new_word

def remove_letters(word, num):
    new_word = word[::num+1]
    return new_word

def shift_characters(word, num):
    new_word = ""
    for char in word:
        new_word = new_word + chr(ord(char)+num)
    return new_word
