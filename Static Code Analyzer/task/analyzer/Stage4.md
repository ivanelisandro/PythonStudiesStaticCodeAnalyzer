# Stage 2:

Add naming rules:
- S007: Too many spaces after construction_name (def or class);
- S008: Class name class_name should be written in CamelCase;
- S009: Function name function_name should be written in snake_case.


## Generic examples:
```
# a simple class
class MyClass:
    pass

# a class based on inheritance
class MyClass(AnotherClass):
    pass
    
# a simple function
def do_magic():
    pass
```

## Example input:
```
class  Person:
    pass

class user:

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    @staticmethod
    def _print1():
        print('q')

    @staticmethod
    def Print2():
        print('q')
```

## Example output:
```
/path/to/file/script.py: Line 1: S007 Too many spaces after 'class'
/path/to/file/script.py: Line 4: S008 Class name 'user' should use CamelCase
/path/to/file/script.py: Line 15: S009 Function name 'Print2' should use snake_case
```