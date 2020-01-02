import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yes_no = str(raw_input("Did you mean %s instead? Enter y for yes for n for no. " % get_close_matches(word, data.keys())[0]))
        if yes_no == "y" or "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yes_no == "N" or "n":
            return "We couldn't find your word, try again!"
        else:
            return "We didn't understand your entry.:("
    else:
        return "The word doesn't exit. Please double check it."

entry = str(raw_input("Would you like to enter a word into dictionary, y for yes, n for no. "))

while entry == "Y" or entry == "y":
    word = raw_input("Enter a word: ")
    output = (translate(word))
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(item)
    new_entry = str(raw_input("Would you like to enter another word? y = yes n = no. "))
    entry = new_entry
   



