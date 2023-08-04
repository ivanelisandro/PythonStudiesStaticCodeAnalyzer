from nltk import regexp_tokenize

sentence = input()
index = int(input())
words = regexp_tokenize(sentence, "[A-z]+")

print(words[index])
