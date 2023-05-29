# InternPE-PyIntern-Tasks

**Task 1: Tic Tac Toe Game**


**Description**:- 

We start by creating an empty board list with 9 elements representing the positions of the Tic Tac Toe board.

'print_board()' function is defined to display the current state of the board.

'check_winner()' function checks if any player has won the game by checking the rows, columns, and diagonals of the board.

'play_game()' function handles the main logic of the game. It starts with the current player as 'X' and continues until the game is over.

Inside the game loop, the board is printed, and the current player is prompted for their move.

The entered position is validated to ensure it is within the valid range and not already occupied. If invalid, an error message is printed, and the loop continues.

If the move is valid, the board is updated with the current player's symbol ('X' or 'O') at the chosen position.

After each move, we check if any player has won by calling check_winner(). If a winner is found, the winner's symbol is displayed, and the game ends.

If the board is full and no winner is found, it is considered a tie, and the game ends.

If the game is not over, the current player is switched to the other symbol (from 'X' to 'O' or vice versa), and the loop continues.

Finally, the game starts by calling play_game().
