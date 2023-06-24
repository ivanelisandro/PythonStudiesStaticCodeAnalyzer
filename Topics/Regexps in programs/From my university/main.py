import re 

string = input()
pattern = r'From: [\w{1,}\._-]+@ucsc\.cl'
print(re.match(pattern, string) is not None)
