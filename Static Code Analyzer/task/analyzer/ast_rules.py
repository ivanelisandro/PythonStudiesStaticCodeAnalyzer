from abc import abstractmethod
import ast


class AstBasedRule:
    def __init__(self, code, message):
        self.code = code
        self.message = message

    @abstractmethod
    def verify(self, lines):
        yield None

    def get_error(self, index):
        return index, f"Line {index}: {self.code} {self.message}"


class ArgumentShouldUseSnakeCase(AstBasedRule):
    def __init__(self):
        super().__init__("S010", "")

    def verify(self, lines):
        tree = ast.parse(lines)

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                for argument in node.args.args:
                    has_upper = any(c.isupper() for c in argument.arg)
                    if has_upper:
                        self.message = f"Argument name '{argument.arg}' should be snake_case."
                        yield super().get_error(node.lineno)


class VariableShouldUseSnakeCase(AstBasedRule):
    def __init__(self):
        super().__init__("S011", "")

    def verify(self, lines):
        functions_lines = []

        tree = ast.parse(lines)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions_lines.extend(range(node.lineno, node.end_lineno + 1))
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store) and node.lineno in functions_lines:
                has_upper = any(c.isupper() for c in node.id)
                if has_upper:
                    self.message = f"Variable '{node.id}' in function should be snake_case."
                    yield super().get_error(node.lineno)


class ArgumentIsMutable(AstBasedRule):
    def __init__(self):
        super().__init__("S012", "Default argument value is mutable.")

    def verify(self, lines):
        tree = ast.parse(lines)

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                for default_value in node.args.defaults:
                    is_mutable = (isinstance(default_value, ast.List) or
                                  isinstance(default_value, ast.Dict) or
                                  isinstance(default_value, ast.Set))
                    if is_mutable:
                        yield super().get_error(node.lineno)


class AstBasedRules:
    all = [ArgumentShouldUseSnakeCase(),
           VariableShouldUseSnakeCase(),
           ArgumentIsMutable()]
