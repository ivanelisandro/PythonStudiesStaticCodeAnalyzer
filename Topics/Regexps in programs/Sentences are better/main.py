import re
string = input()

pattern = r"\w[\w\s',-]+"
x = re.findall(pattern, string)

print(*x, sep='\n')
