import re

string = input()
pattern = r'(([0-2][1-9])|(3[01]))\/((0[1-9])|1[0-2])\/([12][0-9]{3})'

print(bool(re.match(pattern, string)))
