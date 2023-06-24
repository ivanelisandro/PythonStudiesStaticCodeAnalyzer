import re


def check_letter(letter_to_check, text):
    pattern = f"({letter_to_check})"
    result = re.findall(pattern, text)
    if result:
        print(f"{letter_to_check}: {len(result)}")


letters = ["A", "C", "G", "T"]
string = input()
for letter in letters:
    check_letter(letter, string)
