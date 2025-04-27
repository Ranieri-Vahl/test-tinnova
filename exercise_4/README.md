# Exercise 4 - Sum of Multiples of 3 or 5

This project calculates the sum of all natural numbers below a given limit that are multiples of 3 or 5.

---

## Project Structure

exercise4/
├── multiples_sum_calculator.py      # Classe MultiplesSumCalculator
└── README.md                        # Explicação do exercício
├── sum_multiples_interactive.py     # Versão interativa (usuário escolhe)
├── sum_multiples.py                 # Versão simples (número fixo)

---

## 1. Simple Version (`sum_multiples.py`)

- Calculates the sum of all multiples of 3 or 5 below a **predefined limit** set directly in the code.
- To change the limit, edit the `limit` variable inside the file.
- Designed for quick demonstration **without user interaction**.

### Example

For `10`, the output will be:

"The sum of all multiples of 3 or 5 below 10 is: 23"

---

## 2. Interactive Version (`sum_multiples_interactive.py`)

- Prompts the user to enter a non-negative integer.
- Calculates and displays the sum for each input entered.
- Allows the user to exit the program by typing `q`.

### Example

Enter a non-negative integer to calculate the sum of multiples of 3 or 5 (or 'q' to quit): 10 
The sum of all multiples of 3 or 5 below 10 is: 23

Enter a non-negative integer to calculate the sum of multiples of 3 or 5 (or 'q' to quit): 20 
The sum of all multiples of 3 or 5 below 20 is: 78

Enter a non-negative integer to calculate the sum of multiples of 3 or 5 (or 'q' to quit): q 
Goodbye!

---

## How to Run

Open a terminal and execute:

```bash
python sum_multiples.py

 or

python sum_multiples_interactive.py
```