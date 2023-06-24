class Rule:
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def verify(self, index, line_content):
        return f"Line {index}: {self.code} {self.message}"


class LineTooLongRule(Rule):
    max_characters = 79

    def __init__(self):
        super().__init__("S001", f"The line has more than {self.max_characters} characters.")

    def verify(self, index, line_content):
        #print(line_content)
        #print(len(line_content))
        if len(line_content) <= self.max_characters:
            return None

        return super().verify(index, line_content)


class RulesValidator:
    rule = LineTooLongRule()

    def validate(self, lines):
        if not lines:
            return

        for index, line_content in enumerate(lines, start=1):
            error = self.rule.verify(index, line_content)
            if error:
                print(error)
