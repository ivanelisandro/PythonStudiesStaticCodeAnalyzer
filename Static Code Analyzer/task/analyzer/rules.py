from abc import abstractmethod
import re


class Patterns:
    ignore_strings = r"(?<!\\)'([\w\ \?\!\{\},;:\.]|(\\'))+(?<!\\)'"
    ignore_comments = r"\#.+"
    whitespaces_exact = r"(\ )*"
    comment_spaces = r"(\ +)\#.+"
    comment_no_spaces = r"([\w\):])\#.+"
    todo_comments = r"\# TODO.*"


class Rule:
    def __init__(self, code, message):
        self.code = code
        self.message = message

    @abstractmethod
    def verify(self, index, line_content):
        return None

    def get_error(self, index):
        return f"Line {index}: {self.code} {self.message}"


class LineTooLong(Rule):
    max_characters = 79

    def __init__(self):
        super().__init__("S001", f"The line has more than {self.max_characters} characters.")

    def verify(self, index, line_content):
        if len(line_content) <= self.max_characters:
            return None

        return super().get_error(index)


class Indentation(Rule):
    multiple_of = 4

    def __init__(self):
        super().__init__("S002", f"Indentation must be multiple of {self.multiple_of}.")

    def verify(self, index, line_content):
        match_found = re.match(Patterns.whitespaces_exact, line_content)
        if not match_found:
            return None

        group = match_found.group()
        if len(group) % self.multiple_of == 0:
            return None

        return super().get_error(index)


class Semicolon(Rule):
    def __init__(self):
        super().__init__("S003", f"Unnecessary semicolon after statement.")

    def verify(self, index, line_content):
        filtered_line = re.sub(Patterns.ignore_strings, "", line_content)
        filtered_line = re.sub(Patterns.ignore_comments, "", filtered_line)
        if ";" not in filtered_line:
            return None

        return super().get_error(index)


class SpacesBeforeComment(Rule):
    required_spaces = 2

    def __init__(self):
        super().__init__("S004", f"There must be {self.required_spaces} spaces before inline comments.")

    def verify(self, index, line_content):
        filtered_line = re.sub(Patterns.ignore_strings, "", line_content)
        comment_with_spaces = re.search(Patterns.comment_spaces, filtered_line)
        comment_no_spaces = re.search(Patterns.comment_no_spaces, filtered_line)

        if not comment_with_spaces and not comment_no_spaces:
            return None

        if comment_with_spaces:
            group = comment_with_spaces.group(1)
            if len(group) >= self.required_spaces:
                return None

        return super().get_error(index)


class Todo(Rule):
    def __init__(self):
        super().__init__("S005", f"TODO found.")

    def verify(self, index, line_content):
        match_found = re.search(Patterns.todo_comments, line_content, re.IGNORECASE)
        if not match_found:
            return None

        return super().get_error(index)


class BlankLinesExcess(Rule):
    max_accepted = 2
    blank = '\n'

    def __init__(self):
        self.count_blank = 0
        super().__init__("S006", f"More than {self.max_accepted} blank lines preceding code.")

    def verify(self, index, line_content):
        if line_content == self.blank:
            self.count_blank += 1
            return None

        if self.count_blank <= self.max_accepted:
            self.count_blank = 0
            return None

        self.count_blank = 0
        return super().get_error(index)


class RulesValidator:
    rules = [LineTooLong(), Indentation(),
             Semicolon(), SpacesBeforeComment(),
             Todo(), BlankLinesExcess()]

    def validate(self, lines):
        if not lines:
            return

        for index, line_content in enumerate(lines, start=1):
            for rule in self.rules:
                error = rule.verify(index, line_content)
                if error:
                    print(error)
