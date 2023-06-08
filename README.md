# InternPE-PyIntern-Tasks

**#Task 1: Tic Tac Toe Game**

**Description**:- 

•	We start by creating an empty board list with 9 elements representing the positions of the Tic Tac Toe board.
•	'print_board()' function is defined to display the current state of the board.
•	'check_winner()' function checks if any player has won the game by checking the rows, columns, and diagonals of the board.
•	'play_game()' function handles the main logic of the game. It starts with the current player as 'X' and continues until the game is over.
•	Inside the game loop, the board is printed, and the current player is prompted for their move.
•	The entered position is validated to ensure it is within the valid range and not already occupied. If invalid, an error message is printed, and the loop continues.
•	If the move is valid, the board is updated with the current player's symbol ('X' or 'O') at the chosen position.
•	After each move, we check if any player has won by calling check_winner(). If a winner is found, the winner's ymbol is displayed, and the game ends.
•	If the board is full and no winner is found, it is considered a tie, and the game ends.
•	If the game is not over, the current player is switched to the other symbol (from 'X' to 'O' or vice versa), and the loop continues.
•	Finally, the game starts by calling play_game().

**#Task 2: Digital Clock**

**Description**:-
•	We start code by implementing a digital clock using Python and the Tkinter library. The digital clock displays the current time and updates it every second.
•	The clock is displayed in a graphical user interface (GUI) window created using Tkinter. The clock's appearance can be customized with different font styles, colors, and background options.
•	The code begins by importing the necessary modules: tkinter, time, and messagebox. Tkinter is used for creating the GUI, time is used for getting the current time, and messagebox is used to display information boxes.
•	The update_time function is defined to retrieve the current time and update the clock label with the new time every second. This function is scheduled to run repeatedly using the after method from Tkinter.
•	The toggle_fullscreen function is defined to toggle the fullscreen mode of the application. It changes the fullscreen variable and uses the attributes method of the root window to switch between fullscreen and windowed mode.
•	The exit_app function is defined to destroy the root window and exit the application when the "Exit" option is selected from the "File" menu.
•	The about function displays a message box with information about the digital clock application when the "About" option is selected from the "Help" menu.
•	The root window is created using tk.Tk() and titled "Digital Clock".
•	The clock label is created using the Label widget from Tkinter. It is initially set to display the current time with a specified font style, foreground color (text color), and background color. The label is then packed into the root window.
•	Two buttons are created: one for toggling fullscreen mode and another for changing the clock's background color. These buttons are packed into the root window as well.
•	A menu bar is created using the Menu widget. Two menus, "File" and "Help", are added to the menu bar.
•	The "File" menu contains a single option, "Exit", which calls the exit_app function when selected.
•	The "Help" menu contains a single option, "About", which calls the about function when selected.
