'''
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
'''

#Function for generation of magic square
def generateSquare(n):
    #Array with all positions intialized as zero
    magicSquare = [[0 for x in range(n)]
                   for y in range(n)]
    magicSquarevect = []
    # Initializing the position on Magic Square for digit 1
    i = n / 2
    j = n - 1
    # Fill the magic square by placing values
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:#Calculated row position is -1 and column position is n, new position would be (0,n-2)
            j = n - 2
            i = 0
        else:
            # If next number would go out of right side wrap around to start position
            if j == n:
                j = 0
            # If next number would go out of upper side wrap around to bottom
            if i < 0:
                i = n - 1
        if magicSquare[int(i)][int(j)]: #If calculated position (i,j) already taken, new position is (i+1,j-2)
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1
        #Next Position calculated by decreasing row number and increasing column number.
        j = j + 1
        i = i - 1
    # Printing magic square
    print("Generation of "+str(n)+ " X "+str(n)+" Magic Square")
    for i in range(0, n):
        for j in range(0, n):
            #print(magicSquare[i][j],end=' ')
            magicSquarevect.append(magicSquare[i][j])
        #print()
    print(' --- --- ---')
    for i in range(1, 10):
        print('| ' + str(magicSquarevect[i-1]) + ' ', end='')
        if (i % 3 == 0):
            print('|')
            print(' --- --- ---')
    return(magicSquarevect)
#Checking if the position passed is corner or not
def corner_checker(n):
    if(n==2 or n==4 or n==6 or n==8):
        return True
    else:
        return False
n = 3
#Generation of 3*3 Magic Square
magicSquarevect=generateSquare(n)

print("Guidelines of TIC-TAC-TOE:")
print("1.The first player starts with X")
print("2.The lists containing human and computer choices have values with respect to the generated magic square.")
print("3.Position board for your reference:")
print(' --- --- ---')
for i in range(1,10):
    print('| ' + str(i)+' ', end='')
    if (i % 3 == 0):
        print('|')
        print(' --- --- ---')
print("Do you want to go first.?")
choice=(input("Enter 1 if yes else enter any other key."))

#Function for generating board positions taking as input vectors containing human and computer choices
def display(A,B):
    vect_to_display=[]
    for i in range(0,len(magicSquarevect)):
        if(magicSquarevect[i] in A):
            vect_to_display.append('X')#if position in A, add in vector
        elif(magicSquarevect[i] in B):
            vect_to_display.append('O')#if position in B, add in vector
        else:
            vect_to_display.append(' ')#this position is empty
    print(' --- --- ---')
    for i in range(0,len(vect_to_display)):
        print('| '+vect_to_display[i]+' ', end='')
        if((i+1)%3==0):
            print('|')
            print(' --- --- ---')

#Function returning all possible winning positions taking as input vectors containing human and computer choices
def win_possibility(A,B):
    D=[]
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            diff=15-A[i]-A[j]
            if(diff>0 and diff<=9):
                if(diff not in B):
                    D.append(diff)
    return D

#Function mapping user inputs to get cooresponding magic square values
def map(n):
    if(n==1):
        return 2
    if (n == 2):
        return 7
    if (n == 3):
        return 6
    if (n == 4):
        return 9
    if (n == 5):
        return 5
    if (n == 6):
        return 1
    if (n == 7):
        return 4
    if (n == 8):
        return 3
    if (n == 9):
        return 8
    else:
        return 0

#Function returning the pairs of empty positions for any position that has sum 15 taking as input the choices list and the position.
def possible_pairs(cho,pos):
    pairs=[]
    for i in range(0,9):
        for j in range(0,9):
            temp=magicSquarevect[i]+magicSquarevect[j]
            if(temp+pos==15):
                if(magicSquarevect[i] not in cho and magicSquarevect[j] not in cho):
                    pairs.append((magicSquarevect[i],magicSquarevect[j]))
    return pairs

if(choice!='1'):#If user does not choose to go first
    Computer_choices = []#List containing the computer position choices
    Human_choices = []#List containing the human position choices
    choices = []#List containing all positions occupied at any point
    Computer_choices.append(5)#Placing at center
    choices.append(5)#Adding choice to the list
    print("COMPUTER'S TURN")
    display(Computer_choices,Human_choices)#Displaying the board
    print("Human Choice", Human_choices)
    print("Computer Choice", Computer_choices)
    while(True):
        human_input=map(int(input("Enter the position you want to play your turn.")))#Map human input to magic square values
        if((human_input not in choices) and (human_input>0 and human_input<=9)):#If the choice is valid
            break
        print("Choice invalid.")
    Human_choices.append(human_input)
    choices.append(human_input)
    print("YOUR TURN")
    display(Computer_choices,Human_choices)
    print("Human Choice", Human_choices)
    print("Computer Choice", Computer_choices)
    corner_chosen=0 #Variable keeping track of the first corner chosen by computer
    if(human_input==2 or human_input==8 or human_input==4 or human_input==6):
        Computer_choices.append(10-human_input)#Selecting opposite corner to human input
        choices.append(10-human_input)
        corner_chosen=10-human_input
        print("COMPUTER'S TURN")
        display(Computer_choices, Human_choices)
        print("Human Choice", Human_choices)
        print("Computer Choice", Computer_choices)
    else:
        Computer_choices.append(6)#Selecting one corner
        choices.append(6)
        corner_chosen=6
        print("COMPUTER'S TURN")
        display(Computer_choices, Human_choices)
        print("Human Choice", Human_choices)
        print("Computer Choice", Computer_choices)
    while(True):
        #print("Human Choice",Human_choices)
        #print("Computer Choice",Computer_choices)
        #print("Choices made so far:",choices)
        if(len(choices)==9):#If all choices have been exhausted and no winning situation has yet occured
            print("Game Draw")
        while(True):
            human_input = map(int(input("Enter the position you want to play your turn.")))
            if ((human_input not in choices) and (human_input > 0 and human_input <=9)):
                break
            print("Choice invalid.")
        Human_choices.append(human_input)
        choices.append(human_input)
        print("YOUR TURN")
        display(Computer_choices, Human_choices)
        print("Human Choice", Human_choices)
        print("Computer Choice", Computer_choices)
        possible_win=win_possibility(Computer_choices,choices)#Obtain list of winning positions for computer
        if(len(possible_win)==0):#If computer cannot win
            possible_win_foruser=win_possibility(Human_choices,choices)#Check the list of winning positions for user
            if(len(possible_win_foruser)>0):#Computer blocks winning position of user
                Computer_choices.append(possible_win_foruser[0])
                choices.append(possible_win_foruser[0])
                print("COMPUTER'S TURN")
                display(Computer_choices, Human_choices)
                print("Human Choice", Human_choices)
                print("Computer Choice", Computer_choices)
            else:#Neither user nor computer can win
                if(corner_chosen!=0):#Computer has already chosen a corner once
                    pairs_position=possible_pairs(choices,corner_chosen)
                    if(len(pairs_position)!=0):
                        Computer_choices.append(pairs_position[0][0])
                        choices.append(pairs_position[0][0])
                        print("COMPUTER'S TURN")
                        display(Computer_choices, Human_choices)
                        print("Human Choice", Human_choices)
                        print("Computer Choice", Computer_choices)
                    else:
                        pairs_position=possible_pairs(choices,5)
                        if (len(pairs_position) != 0):
                            Computer_choices.append(pairs_position[0][0])
                            choices.append(pairs_position[0][0])
                            print("COMPUTER'S TURN")
                            display(Computer_choices, Human_choices)
                            print("Human Choice", Human_choices)
                            print("Computer Choice", Computer_choices)
                        else:
                            Computer_choices.append(45 - sum(choices))
                            choices.append(45 - sum(choices))
                            print("COMPUTER'S TURN")
                            display(Computer_choices, Human_choices)
                            print("Human Choice", Human_choices)
                            print("Computer Choice", Computer_choices)

        else:
            Computer_choices.append(possible_win[0])
            choices.append(possible_win[0])
            print("COMPUTER'S TURN")
            display(Computer_choices, Human_choices)
            print("Human Choice", Human_choices)
            print("Computer Choice", Computer_choices)
            print("Computer Wins.")
            break
else:
    choices = []#List containing already taken positions
    Computer_choices = []#List containing Computer taken positions
    Human_choices = []#List containing Human taken positions
    User_Corner = 0  #Initializing user corner variable to track user chosen corner
    while (True):
        human_input = map(int(input("Enter the position you want to play your turn.")))#Mapping user input to appropriate magic square values
        if ((human_input not in choices) and (human_input > 0 and human_input <=9)):#If human inputs are valid
            if(corner_checker(human_input)):#If the human input is a corner
                User_Corner=human_input #Designate corner as that input
            break
        print("Choice invalid.")#When choice is not valid
    corner_chosen = 0 #Variable keeping track of the first corner chosen by computer
    Human_choices.append(human_input) #Adding human input to the list
    choices.append(human_input)     #Adding human input to choices list
    print("YOUR TURN")
    display(Human_choices,Computer_choices)#Displaying the board
    print("Human Choice", Human_choices)
    print("Computer Choice", Computer_choices)
    if(human_input==5): #If human selects middle position
        Computer_choices.append(6) #Computer choses the corner position
        choices.append(6)
        corner_chosen=6 #Corner chosen by computer is set
        print("COMPUTER'S TURN")
        display(Human_choices, Computer_choices) # Display the board
        print("Human Choice", Human_choices)
        print("Computer Choice", Computer_choices)
    else:
        Computer_choices.append(5) #If user does not select middle point, Computer selects middle point
        choices.append(5)
        print("COMPUTER'S TURN")
        display(Human_choices, Computer_choices)#Display the board
        print("Human Choice", Human_choices)
        print("Computer Choice", Computer_choices)
        while (True):
            human_input = map(int(input("Enter the position you want to play your turn.")))  # Mapping user input to appropriate magic square values
            if ((human_input not in choices) and (human_input > 0 and human_input <= 9)):  # If human inputs are valid
                if (corner_checker(human_input)):  # If the human input is a corner
                    User_Corner = human_input  # Designate corner as that input
                break
            print("Choice invalid.")  # When choice is not valid
        Human_choices.append(human_input)
        print("YOUR TURN")
        choices.append(human_input)
        display(Human_choices, Computer_choices)
        print("Human Choice", Human_choices)
        print("Computer Choice", Computer_choices)
        middle=False #Variable checking if middle opposite positions are occupied by human or not
        if(Human_choices[0]==1 and Human_choices[1]==9):
            middle=True
        elif(Human_choices[0]==9 and Human_choices[1]==1):
            middle=True
        elif(Human_choices[0]==7 and Human_choices[1]==3):
            middle=True
        elif(Human_choices[0]==3 and Human_choices[1]==7):
            middle=True
        if(middle):#If any of the middle opposite positions are occupied, corner is selected
            Computer_choices.append(6)
            choices.append(6)
            print("COMPUTER'S TURN")
            display(Human_choices, Computer_choices) #Displaying the board
            print("Human Choice", Human_choices)
            print("Computer Choice", Computer_choices)
        elif ((Human_choices[0] == 7 and Human_choices[1] == 1)or(Human_choices[0] == 1 and Human_choices[1] == 7)): #If these positions are occupied by human, corner between them is taken by computer
            Computer_choices.append(6)
            choices.append(6)
            print("COMPUTER'S TURN")
            display(Human_choices, Computer_choices) #Displaying the board
            print("Human Choice", Human_choices)
            print("Computer Choice", Computer_choices)
        elif ((Human_choices[0] == 7 and Human_choices[1] == 9)or(Human_choices[0] == 9 and Human_choices[1] == 7)):#If these positions are occupied by human, corner between them is taken by computer
            Computer_choices.append(2)
            choices.append(2)
            print("COMPUTER'S TURN")
            display(Human_choices, Computer_choices) #Displaying the board
            print("Human Choice", Human_choices)
            print("Computer Choice", Computer_choices)
        elif ((Human_choices[0] == 9 and Human_choices[1] == 3)or(Human_choices[0] == 3 and Human_choices[1] == 9)):#If these positions are occupied by human, corner between them is taken by computer
            Computer_choices.append(4)
            choices.append(4)
            print("COMPUTER'S TURN")
            display(Human_choices, Computer_choices) #Displaying the board
            print("Human Choice", Human_choices)
            print("Computer Choice", Computer_choices)
        elif ((Human_choices[0] == 3 and Human_choices[1] == 1)or(Human_choices[0] == 1 and Human_choices[1] == 3)):#If these positions are occupied by human, corner between them is taken by computer
            Computer_choices.append(8)
            choices.append(8)
            print("COMPUTER'S TURN") #Displaying the board
            display(Human_choices, Computer_choices)
            print("Human Choice", Human_choices)
            print("Computer Choice", Computer_choices)
        elif ((Human_choices[0] == 2 and Human_choices[1] == 8)or(Human_choices[0] == 8 and Human_choices[1] == 2)):#If these positions are occupied by human, corner between them is taken by computer
            Computer_choices.append(7)
            choices.append(7)
            print("COMPUTER'S TURN")
            display(Human_choices, Computer_choices)
            print("Human Choice", Human_choices)
            print("Computer Choice", Computer_choices)
        elif ((Human_choices[0] == 6 and Human_choices[1] == 4)or(Human_choices[0] == 4 and Human_choices[1] == 6)):#If these positions are occupied by human, corner between them is taken by computer
            Computer_choices.append(7)
            choices.append(7)
            print("COMPUTER'S TURN")
            display(Human_choices, Computer_choices)
            print("Human Choice", Human_choices)
            print("Computer Choice", Computer_choices)
        else:
            possible_win_foruser = win_possibility(Human_choices, choices) #Possibile positions for user to win
            if (len(possible_win_foruser) > 0): #If user can win(Length of possible positions for user to win is more than 0)
                Computer_choices.append(possible_win_foruser[0]) #Block the winning position of user
                choices.append(possible_win_foruser[0])
                print("COMPUTER'S TURN")
                display(Human_choices, Computer_choices)#Displaying the board
                print("Human Choice", Human_choices)
                print("Computer Choice", Computer_choices)
            else:
                if(User_Corner!=0):#To place computer choice on the opposite position of the user's corner
                    Computer_choices.append(10-User_Corner)
                    choices.append(10-User_Corner)
                    print("COMPUTER'S TURN")
                    display(Human_choices, Computer_choices)#Displaying the board
                    print("Human Choice", Human_choices)
                    print("Computer Choice", Computer_choices)
            corner_chosen=0
    while(True): #Loop for checking Winning of Computer and User
        if (len(choices) == 9):#When length of choices exhausted reaches 9, the game is drawn
            print("Game Draw")
            break
        while (True):
            human_input = map(int(input("Enter the position you want to play your turn.")))  # Mapping user input to appropriate magic square values
            if ((human_input not in choices) and (human_input > 0 and human_input <= 9)):  # If human inputs are valid
                if (corner_checker(human_input)):  # If the human input is a corner
                    User_Corner = human_input  # Designate corner as that input
                break
            print("Choice invalid.")
        Human_choices.append(human_input)
        print("YOUR TURN")
        choices.append(human_input)
        display(Human_choices, Computer_choices)#Displaying the board
        print("Human Choice", Human_choices)
        print("Computer Choice", Computer_choices)
        if (len(choices) == 9):
            print("Game Draw")#Game is drawn
            break
        possible_win = win_possibility(Computer_choices, choices)#List containing all possible win positions for computer
        if (len(possible_win) == 0):#If computer cannot win(Length of possible win=0)
            possible_win_foruser = win_possibility(Human_choices, choices)#List containing all possible win positions for user
            if (len(possible_win_foruser) > 0): #If user can win(Length of possible win for user=0)
                Computer_choices.append(possible_win_foruser[0])#Block the user win position
                choices.append(possible_win_foruser[0])
                print("COMPUTER'S TURN")
                display(Human_choices, Computer_choices)
                print("Human Choice", Human_choices)
                print("Computer Choice", Computer_choices)
                if (len(choices) == 9):
                    print("Game Draw")
                    break
            else:#If neither user nor computer wins
                if (corner_chosen != 0):#If corner chosen by computer is not empty
                    pairs_position = possible_pairs(choices, corner_chosen)#Call possible pair function with regard to corner chosen
                    if (len(pairs_position) != 0):#If the pairs_position is not empty
                        Computer_choices.append(pairs_position[0][0])#Chose any of the empty position from the pair
                        choices.append(pairs_position[0][0])
                        print("COMPUTER'S TURN")
                        display(Human_choices,Computer_choices)#Display the board
                        print("Human Choice", Human_choices)
                        print("Computer Choice", Computer_choices)
                    else:
                        pairs_position = possible_pairs(choices, 5)#Else return the pair positions with respect to the center position
                        if (len(pairs_position) != 0):#If some pairs exist
                            Computer_choices.append(pairs_position[0][0])
                            choices.append(pairs_position[0][0])
                            print("COMPUTER'S TURN")
                            display(Human_choices,Computer_choices)#Display the board
                            print("Human Choice", Human_choices)
                            print("Computer Choice", Computer_choices)
                        else:#For playing the last remaining position on the board in case of a draw
                            Computer_choices.append(45 - sum(choices))
                            choices.append(45 - sum(choices))
                            print("COMPUTER'S TURN")
                            display(Human_choices,Computer_choices)#Display the board
                            print("Human Choice", Human_choices)
                            print("Computer Choice", Computer_choices)
                else:#If both corner positions or both opposite middle positions are empty/not occupied. Place computer choice at any of those positions.
                    if(6 not in choices and 4 not in choices):
                        Computer_choices.append(6)
                        choices.append(6)
                        print("COMPUTER'S TURN")
                        display(Human_choices, Computer_choices)
                        print("Human Choice", Human_choices)
                        print("Computer Choice", Computer_choices)
                    elif(8 not in choices and 2 not in choices):
                        Computer_choices.append(8)
                        choices.append(8)
                        print("COMPUTER'S TURN")
                        display(Human_choices, Computer_choices)
                        print("Human Choice", Human_choices)
                        print("Computer Choice", Computer_choices)
                    elif (7 not in choices and 3 not in choices):
                        Computer_choices.append(7)
                        choices.append(7)
                        print("COMPUTER'S TURN")
                        display(Human_choices, Computer_choices)
                        print("Human Choice", Human_choices)
                        print("Computer Choice", Computer_choices)
                    elif (9 not in choices and 1 not in choices):
                        Computer_choices.append(9)
                        choices.append(9)
                        print("COMPUTER'S TURN")
                        display(Human_choices, Computer_choices)
                        print("Human Choice", Human_choices)
                        print("Computer Choice", Computer_choices)
                    else:
                        corners=[2,4,6,8]#list of all corner positions
                        corner_unchosen=list(set(corners)-(set(choices)&set(corners)))#list containing unchosen corners
                        Computer_choices.append(corner_unchosen[0])#Unchosen corner is selected by computer
                        choices.append(corner_unchosen[0])#Unchosen corner is added to the choices list
                        print("COMPUTER'S TURN")
                        display(Human_choices, Computer_choices)#Displaying the board
                        print("Human Choice", Human_choices)
                        print("Computer Choice", Computer_choices)
                if (len(choices) == 9):
                    print("Game Draw")#Game drawn when all options exhausted
                    break
        else:
            Computer_choices.append(possible_win[0])#Adding at the position where computer wins
            choices.append(possible_win[0])#Adding at the position where computer wins
            print("COMPUTER'S TURN")
            display(Human_choices, Computer_choices)#Displaying the board
            print("Human Choice", Human_choices)
            print("Computer Choice", Computer_choices)
            print("Computer Wins.")
            break
        if (len(choices) == 9):
            print("Game Draw") #When entire options have been used, game is drawn
            break
