# Sudoku Solver

Welcome to the Sudoku Solver repository! Here, you'll find a simple, yet powerful, Python script that can solve any Sudoku puzzle in a matter of seconds.

The project started out as a way to make solving Sudoku puzzles more efficient. In January 2023, I was feeling frustrated due to exams and was looking for a way to refresh my mind. I picked up a newspaper and started solving a Sudoku puzzle, but found it to be time-consuming. That's when the idea for a Sudoku solver came to me.

The script makes use of a backtracking algorithm and the following approach to solve the puzzles:
- 1: Create a board using a list.
- 2: Print the board using a print function.
- 3: Find blank spaces on the board (represented by zeroes) using nested loops.
- 4: Implement rules of Sudoku (checking rows, columns, and 3x3 grids) using separate functions.
- 5: Create a final function that uses the above functions to solve the puzzle. This function uses a recursive approach to fill in the blank spaces and validate the            numbers, returning false if no solution is found.

## Getting Started

To use the script,change the board by your own version of board manually and then simply run it.

