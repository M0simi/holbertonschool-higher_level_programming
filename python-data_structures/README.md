# Python - Data Structures: Lists, Tuples

This project is about learning how to use lists and tuples in Python.

## Concepts Covered

- What are lists and how to use them
- Differences and similarities between lists and strings
- Common list methods and how to use them
- Using lists as stacks and queues
- List comprehensions
- Tuples and when to use them
- What is a sequence
- Tuple packing and unpacking
- The `del` statement

## Requirements

- Python 3.8.5
- Files must start with `#!/usr/bin/python3`
- Code must follow pycodestyle (version 2.7.*)
- No external libraries allowed
- All files must be executable
- Each file must end with a new line

## Example

Function to print all integers in a list:

```python
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))
