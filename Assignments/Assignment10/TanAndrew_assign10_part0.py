#Andrew Tan, 5/3, Section 010, Part 0

#Define dictionary
thesaurus = {
              "happy": "glad",
              "sad"  : "bleak"
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
        split_phrase[index] = str.upper(thesaurus[word])

phrase = " ".join(split_phrase)

#Display output
print(phrase)
