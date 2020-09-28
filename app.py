import json
from difflib import get_close_matches as gcm

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(gcm(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: \n" %
                   gcm(w, data.keys())[0])
        if yn == "Y":
            return data[gcm(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn\'t exists. Please double check the entered word."
        else:
            return "We did not understand you query"
    else:
        return "The word doesn\'t exists. Please double check the entered word."


word = input("Enter a word...\n")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
