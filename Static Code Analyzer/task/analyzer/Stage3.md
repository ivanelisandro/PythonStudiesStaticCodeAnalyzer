# Stage 3:

Process multi-file projects:
- Project directory must now be a command-line argument;
- Example:
```
python code_analyzer.py directory-or-file
```
- Output should contain path to the analyzed file;
- Example:
```
Path: Line X: Code Message
```
- Output lines must be sorted in ascending order by file name, line number, and issue code.
- Ignore Non-Python files;


## Example 1. Only a single file is specified as the input:
```
> python code_analyzer.py /path/to/file/script.py
/path/to/file/script.py: Line 1: S004 At least two spaces required before inline comments
/path/to/file/script.py: Line 2: S003 Unnecessary semicolon
/path/to/file/script.py: Line 3: S001 Too long line
/path/to/file/script.py: Line 3: S003 Unnecessary semicolon
/path/to/file/script.py: Line 6: S001 Too long line
/path/to/file/script.py: Line 11: S006 More than two blank lines used before this line
/path/to/file/script.py: Line 13: S003 Unnecessary semicolon
/path/to/file/script.py: Line 13: S004 At least two spaces required before inline comments
/path/to/file/script.py: Line 13: S005 TODO found
```

## Example 2. The input path is a directory; the output should contain all Python files from it:
```
> python code_analyzer.py /path/to/project
/path/to/project/__init__.py: Line 1: S001 Too long line
/path/to/project/script1.py: Line 1: S004 At least two spaces required before inline comments
/path/to/project/script1.py: Line 2: S003 Unnecessary semicolon
/path/to/project/script2.py: Line 1: S004 At least two spaces required before inline comments
/path/to/project/script2.py: Line 3: S001 Too long line
/path/to/project/somedir/script.py: Line 3: S001 Too long line
/path/to/project/test.py: Line 3: Line 13: S003 Unnecessary semicolon
```