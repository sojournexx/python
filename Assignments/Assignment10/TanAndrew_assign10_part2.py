#Andrew Tan, 5/3, Section 010, Part 2

import random

#Create dictionary from external file
file_obj = open("python_asg10_Roget_Thesaurus.txt", "r")

alldata = file_obj.read()
splitdata = alldata.split("\n")

thesaurus = {}
for i in range(len(splitdata)):
    value = splitdata[i].split(",")
    key = value[0]
    del value[0]
    thesaurus[key] = value

count = len(thesaurus.keys())
print("Total words in thesaurus: {}".format(count))

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
