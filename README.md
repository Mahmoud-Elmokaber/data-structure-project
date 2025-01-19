
# Mathematical Expression Parser and Evaluator
This project is a Python module that parses and evaluates mathematical expressions using a binary tree structure. It supports operations with different precedence levels and parentheses.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction
This project is designed to parse and evaluate mathematical expressions. It uses a binary tree structure to handle different operations and precedence levels, making it easier to evaluate complex expressions.

## Installation
To use this project, simply clone the repository and ensure you have Python installed on your system.

```bash
git clone https://github.com/Mahmoud-Elmokaber/data-structure-project.git
cd Mahmoud-Elmokaber
```
## Usage
Here's an example of how to use the module to evaluate an expression:
```bash
Python
from parser import parse, evaluate

result = evaluate(parse("1 + 2 * 3"))
print(result) # Output: 7.0

result = evaluate(parse("1 + 2 * 3 + 4"))
print(result) # Output: 11.0

result = evaluate(parse("1 + 2 * 3 + 4 * 5"))
print(result) # Output: 27.0

result = evaluate(parse("1 + 2 * 3 + 4 * 5 + 6"))
print(result) # Output: 33.0
```
## Contributing
Contributions are welcome! Please fork the repository and create a pull request to add any features or fix any issues.

## Contact
For any inquiries or support, please reach out to me at mahmoudelmokaber4@gmail.com.
