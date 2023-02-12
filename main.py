import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('omw-1.4')
forbidden = ["indiana","axerophthol", "astatine", "angstrom","arsenic", "adenine", "lapplander", "saami","deoxyadenosine_monophosphate","", " "]
dontchange = ["in", "a", "i", "and", "to", "or", "are"]

def findlongest(word, arr):
  synonyms = []
  max = word
  for syn in wordnet.synsets(word):
    for l in syn.lemmas():
          synonyms.append(l.name())
          if (len(l.name()) > len(max)) and "_" not in l.name() and (l.name().lower() not in forbidden) and word.lower() not in dontchange and not word[0].isupper() and (word not in arr[-1:-100]):
            max = l.name().lower()
  if max != "":
    return max
  else:
    return word

sentence = open("essay.txt", "r").read()
new_sentence = []
sentence_split = sentence.split()
for word in sentence_split:
  new_sentence.append(findlongest(word, new_sentence))
f = open("output.txt", "w")
f.write(" ".join(new_sentence))
f.close()
print("Your essay has been longified.")
