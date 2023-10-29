from ast_rules import AstBasedRules
from rules import Rules
from source_retriever import SourceFile, SourceProject


class RulesValidator:
    rules = Rules.all
    ast_rules = AstBasedRules.all

    def validate(self, path, lines):
        if not lines:
            return

        errors = []
        full_text = ""
        for index, line_content in enumerate(lines, start=1):
            full_text += f"{line_content}"
            for rule in self.rules:
                error = rule.verify(index, line_content)
                if error:
                    errors.append((index, error))

        for rule in self.ast_rules:
            for index, error in rule.verify(full_text):
                if error:
                    errors.append((index, error))

        for index, error in sorted(errors):
            print(f"{path}: {error}")


class ProjectValidator:
    validator = RulesValidator()

    def run(self, project_path):
        for file_path in SourceProject.get_files(project_path):
            lines = SourceFile.get_lines(file_path)

            self.validator.validate(file_path, lines)
