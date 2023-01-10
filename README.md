# sudokuSolver

Story behind this project:
    In a day of january of 2023,I was frustrated that day beacause of my exams.
    However, I was looking for refreshment so, I checked newspaper and was trying to solve sudoku.
    But I felt that it was very time consuming. I had idea to create sudokuSolver.
    
Approach:
    -1:  create a board.(I just use list as board.)
    -2:  A function to print the board.(just using print statement.)
    -3:  A function to find blank place(here it is 0,just using nested loops)
    -4:  A function that define rules of sudoku(checking row,checking colums,and checking 3x3 grid where an element is placed.)
    -5:  A final functionn to solve problem using above functions
            1:get blank place, 
            2:validate a number is right acording to rules at perticulare place
            3:use recursion to solve other positions
            4:if there is not any solution of given borad then return false
            
