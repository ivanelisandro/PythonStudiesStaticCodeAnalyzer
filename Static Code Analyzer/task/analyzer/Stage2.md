# Stage 2:

Add more rules:
- S002: Indentation is not a multiple of four;
- S003: Unnecessary semicolon after a statement (note that semicolons are acceptable in comments);
- S004: Less than two spaces before inline comments;
- S005: TODO found (in comments only and case-insensitive);
- S006: More than two blank lines preceding a code line (applies to the first non-empty line).


## Example input:
```
print('What\'s your name?') # reading an input
name = input();
print(f'Hello, {name}');  # here is an obvious comment: this prints a greeting with a name


very_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
print(very_big_number)



def some_fun():
    print('NO TODO HERE;;')
    pass; # Todo something
```

## Example output:
```
Line 1: S004 At least two spaces required before inline comments
Line 2: S003 Unnecessary semicolon
Line 3: S001 Too long
Line 3: S003 Unnecessary semicolon
Line 6: S001 Too long
Line 11: S006 More than two blank lines used before this line
Line 13: S003 Unnecessary semicolon
Line 13: S004 At least two spaces required before inline comments
Line 13: S005 TODO found
```