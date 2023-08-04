from nltk.tokenize import regexp_tokenize

sentence = input()
pattern = "[A-z'-]+"
print(regexp_tokenize(sentence, pattern))
