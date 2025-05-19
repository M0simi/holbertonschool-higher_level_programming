# Python - Test-driven development

This project is part of the Holberton School curriculum.  
It focuses on the **Test-Driven Development (TDD)** methodology in Python, using **Docstrings** and the **doctest** module.

## 📚 Learning Objectives

- Understand why Python is a great language
- What is an interactive test
- Why testing code is important
- How to write Docstrings that include tests
- How to create and structure documentation for modules and functions
- Basic flags for testing with `doctest`
- How to find and cover edge cases in test scenarios

## 🧪 Project Structure

python-test_driven_development/
│
├── 0-add_integer.py # Function to add two integers
├── tests/
│ └── 0-add_integer.txt # Doctest file to test add_integer function
└── README.md # Project documentation

## ✅ Requirements

- Python 3.8.5 (Ubuntu 20.04 LTS)
- PEP8 compliant (pycodestyle 2.7.\*)
- Use of doctest for testing
- No external imports allowed

## 🚀 How to Test

Use the `doctest` module to run the test cases:

```bash
python3 -m doctest -v ./tests/0-add_integer.txt

## Example

def add_integer(a, b=98):
    """
    Adds two integers or floats (converted to integers).

    Args:
        a: First number (int or float)
        b: Second number (int or float), default is 98

    Returns:
        The sum of a and b as an integer

    Raises:
        TypeError: If a or b are not int or float
    """

---

## ✍️ Author
[Meshari - M0simi](https://github.com/M0simi)
