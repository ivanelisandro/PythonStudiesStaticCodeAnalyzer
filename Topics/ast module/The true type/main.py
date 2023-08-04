import ast

text = input()
evaluation = ast.literal_eval(text)
print(type(evaluation))