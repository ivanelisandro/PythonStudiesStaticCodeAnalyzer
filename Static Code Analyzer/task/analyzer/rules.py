from abc import abstractmethod
import ast
import re


class Patterns:
    ignore_strings = r"(?<!\\)'([\w\ \?\!\{\},;:\.]|(\\'))+(?<!\\)'"
    ignore_comments = r"\#.+"
    whitespaces_exact = r"(\ )*"
    comment_spaces = r"(\ +)\#.+"
    comment_no_spaces = r"([\w\):])\#.+"
    todo_comments = r"\# TODO.*"
    whitespaces_after_class = r"(def|class)\s{2,}"
    class_name = r"class\s{1}(\w{1,})"
    function_name = r"def\s{1}\_*([a-zA-Z0-9]{1,})\_*"


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


class TooManySpacesAfterDefClass(Rule):
    def __init__(self):
        self.name = ""
        super().__init__("S007", "")

    def verify(self, index, line_content):
        excess_found = re.search(Patterns.whitespaces_after_class, line_content)
        if not excess_found:
            return None

        self.message = f"Too many spaces after '{excess_found.group(1)}'."
        return super().get_error(index)


class ClassShouldUseCamelCase(Rule):
    def __init__(self):
        super().__init__("S008", "")

    def verify(self, index, line_content):
        class_found = re.search(Patterns.class_name, line_content)
        if not class_found:
            return None

        class_name = class_found.group(1)
        if class_name[0].isupper() and "_" not in class_name:
            return None

        self.message = f"Class name '{class_name}' should use CamelCase."
        return super().get_error(index)


class FunctionShouldUseSnakeCase(Rule):
    def __init__(self):
        super().__init__("S009", "")

    def verify(self, index, line_content):
        function_found = re.search(Patterns.function_name, line_content)
        if not function_found:
            return None

        function_name = function_found.group(1)
        if not any(character.isupper() for character in function_name):
            return None

        self.message = f"Function name '{function_name}' should use snake_case."
        return super().get_error(index)


class Rules:
    all = [LineTooLong(), Indentation(),
           Semicolon(), SpacesBeforeComment(),
           Todo(), BlankLinesExcess(),
           TooManySpacesAfterDefClass(),
           ClassShouldUseCamelCase(),
           FunctionShouldUseSnakeCase()]
