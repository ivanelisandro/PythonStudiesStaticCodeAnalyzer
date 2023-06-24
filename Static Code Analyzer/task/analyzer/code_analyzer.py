from source_retriever import SourceFile
from rules import RulesValidator

lines = SourceFile.get_lines(input())

validator = RulesValidator()
validator.validate(lines)
