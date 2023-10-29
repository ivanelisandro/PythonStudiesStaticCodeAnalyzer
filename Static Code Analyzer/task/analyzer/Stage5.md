# Stage 5:

Add functions and variables rules:
- S010: Argument name arg_name should be written in snake_case;
- S011: Variable var_name should be written in snake_case;
- S012: The default argument value is mutable.

Details:
- Invalid function name should be output only when the function is defined;
- Invalid variable name should be output only when this variable is assigned a value;
- Only need to check whether the mutable value is directly assigned to an argument;
- If a function contains several mutable arguments, the message should be output only once for this function;
- Variable and argument names are assumed to be valid if they are written in snake_case;
- Initial underscores (_) are also acceptable;

## Function argument example:
```python
def fun1(test=[]):  # default argument value is mutable
    pass


def fun2(test=get_value()):  # you can skip this case to simplify the problem
    pass
```

## Example input:
```python
CONSTANT = 10
names = ['John', 'Lora', 'Paul']


def fun1(S=5, test=[]):  # default argument value is mutable
    VARIABLE = 10
    string = 'string'
    print(VARIABLE)
```

## Example output:
```bash
/path/to/file/script.py: Line 5: S010 Argument name 'S' should be snake_case
/path/to/file/script.py: Line 5: S012 Default argument value is mutable
/path/to/file/script.py: Line 6: S011 Variable 'VARIABLE' in function should be snake_case
```