# 2-D-Tic-Tac-Toe
Implementation of 2-D Tic Tac Toe using concept of Magic Square.

Program:
1.Generating magic square of dimension 3 x 3.
2.Implementing 2-D tic tac toe using magic square concept.
3.Displaying the board position after each turn along with list of contents for both the players.

Our Approach:
$-First we generated 3X3 Magic Square using the function generateSquare()
$-After generation of Magic Square we approached the Tic-Tac-Toe in the following manner:
    We made function win_possibility which we use to find out the winning positions of User/Computer
    #-Case 1: Computer takes the first turn
        Starting position is middle square to maximise the chances of winning of Computer.
        User Input is taken.
        Appropriate choice is made by the computer.
        Again User Input is taken.
        Then the win_possibility function is used to check the winning positions of both Computer and User successively.
        If there is a position for computer to win, Computer chooses that position.
        Else If there is a position for user to win, Computer blocks that position.
        Else depending on the situation Computer chooses the Ideal choice.
    #-Case 2: User takes the first turn
        a)User doesn't choose the middle position
            Computer chooses the middle position.
            Again User Input is taken.
            Then the win_possibility function is used to check the winning positions of both Computer and User successively.
            If there is a position for computer to win, Computer chooses that position.
            Else If there is a position for user to win, Computer blocks that position.
            Else depending on the situation Computer chooses the Ideal choice.
        b) User chooses the middle position
            Computer chooses one of the corners.
            Again User Input is taken.
            Then the win_possibility function is used to check the winning positions of both Computer and User successively.
            If there is a position for computer to win, Computer chooses that position.
            Else If there is a position for user to win, Computer blocks that position.
            Else depending on the situation Computer chooses the Ideal choice.
