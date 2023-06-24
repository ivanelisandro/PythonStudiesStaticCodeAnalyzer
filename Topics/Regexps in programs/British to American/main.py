import re

string = input()
replaced = re.sub('ou', 'o', string)
print(replaced)
