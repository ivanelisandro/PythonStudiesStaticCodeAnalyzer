from nltk.tokenize import sent_tokenize, regexp_tokenize

text = input()
index = int(input())
sentences = sent_tokenize(text)
selected = regexp_tokenize(sentences[index], "[A-z']+")
print(selected)
