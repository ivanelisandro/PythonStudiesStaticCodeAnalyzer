from rules import Rules
from source_retriever import SourceFile, SourceProject


class RulesValidator:
    rules = Rules.all

    def validate(self, path, lines):
        if not lines:
            return

        for index, line_content in enumerate(lines, start=1):
            for rule in self.rules:
                error = rule.verify(index, line_content)
                if error:
                    print(f"{path}: {error}")


class ProjectValidator:
    validator = RulesValidator()

    def run(self, project_path):
        for file_path in SourceProject.get_files(project_path):
            lines = SourceFile.get_lines(file_path)

            self.validator.validate(file_path, lines)
