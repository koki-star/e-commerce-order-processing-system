# E-Commerce Order Processing System

## Project overview
This project stores e-commerce orders in a singly linked list. It appends orders in the order they arrive, displays them from first to last, reverses the node links, and then displays the most recent orders first.

## How to run
From the project folder, run:

```bash
python3 order_system.py
```

## How to run tests
From the project folder, run:

```bash
python3 -m unittest discover tests
```

## Clarifying questions
- Does the instructor require a specific programming language for the project?
- If no language is required, is Python acceptable for submission?
- Should `display()` return the orders, print the orders, or is either format acceptable?
- Does the instructor want the GitHub repository to include only source code and docs, or also the video demo link in the README?

## Time and space complexity
- `append(order)`: Time `O(n)`, Space `O(1)`
- `display()`: Time `O(n)`, Space `O(n)` because it returns a list of orders for output
- `reverse()`: Time `O(n)`, Space `O(1)` because it changes node links directly
