import re

string = input()
capitalized_pattern = r'[A-Z]\w+'
digits_pattern = r'\d{1,}'

capitalized = re.findall(capitalized_pattern, string)
digits = re.findall(digits_pattern, string)

print("Capitalized words: ", end='')
print(*capitalized, sep=', ')
print("Digits: ", end='')
print(*digits, sep=', ')
