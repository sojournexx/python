#Andrew Tan, 5/3, Section 010, Part 1

import random

#Define dictionary
thesaurus = {
              "happy":["glad",  "blissful", "ecstatic", "at ease"],
              "sad"  :["bleak", "blue",     "depressed"]
            }

#Request user input
phrase = str.lower(input("Enter a phrase: "))

#Replace words found in dictionary
phrase = phrase.replace(",", "")
phrase = phrase.replace(".", "")
phrase = phrase.replace("!", "")

split_phrase = phrase.split(" ")

for word in split_phrase:
    if word in thesaurus:
        index = split_phrase.index(word)
        split_phrase[index] = str.upper(thesaurus[word][random.randint(0, len(thesaurus[word])-1)])

phrase = " ".join(split_phrase)

#Display output
print(phrase)
