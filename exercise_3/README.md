# Exercise 3 - Factorial Calculator

exercise3/
├── factorial_calculator.py        # Class definition (FactorialCalculator)
├── factorial_interactive.py       # Interactive version (user input)
├── factorial.py                   # Simple version (predefined number)
└── README.md

This project contains two versions of a program that calculates the factorial of a number.

---

## 1. Simple Version (`factorial.py`)

- Calculates the factorial of a **predefined number** inside the code.
- To change the number, simply edit the `number` variable inside the file.
- Designed for quick demonstration **without user interaction**.

## Example
For `5`, the output will be:

"The factorial of 5 is: 120"


## 2. Interactive Version (`factorial_interactive.py`)

 - Prompts the user to enter a non-negative integer.
 - Calculates and displays the factorial for each input entered.
 - Allows the user to exit the program by typing q.

## Example

Enter a non-negative integer to calculate its factorial (or 'q' to quit): 4
The factorial of 4 is: 24

Enter a non-negative integer to calculate its factorial (or 'q' to quit): 6
The factorial of 6 is: 720

Enter a non-negative integer to calculate its factorial (or 'q' to quit): q
Goodbye!

## How to run

```bash
python factorial.py

or

python factorial_interactive.py
