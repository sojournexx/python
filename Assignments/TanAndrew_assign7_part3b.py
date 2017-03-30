#Andrew Tan, 3/30, Section 010, Part 3b

import random

#Define functions
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

#Ask user for mode selection and validate
while True:
    mode = str(input("(e)ncode, (d)ecode or (q)uit: "))
    
    #Encryption
    if mode == "e":
        while True:
            key = int(input("Enter a number between 1 and 5: "))
            if key >= 1 and key <= 5:
                break
        phrase = str(input("Enter a phrase to encode: "))
        encrypted_word = shift_characters(add_letters(phrase, key), key)
        print("Your encoded word is: %s\n" %(encrypted_word))
    
    #Decryption
    elif mode == "d":
        while True:
            key = int(input("Enter a number between 1 and 5: "))
            if key >= 1 and key <= 5:
                break
        phrase = str(input("Enter a phrase to decode: "))
        decrypted_word = shift_characters(remove_letters(phrase, key), -key)
        print("Your decoded word is: %s\n" %(decrypted_word))
    
    #Exit program
    elif mode == "q":
        break

