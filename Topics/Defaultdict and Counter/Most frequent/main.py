from collections import Counter


text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        + "I may be off my dot but I want a cup of coffee from a proper coffee pot.")

number = int(input())
counter = Counter(text.split())

for word_count in counter.most_common(number):
    print(*word_count)
