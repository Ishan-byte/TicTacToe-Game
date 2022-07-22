#overwriting sum function
def sum(a, b, c):
    return a + b + c

#function that prints the board
def printBoard(xState, zState):

    #messy variables
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three= 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)

    #printing the board
    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")


#Winner check function
def checkWin(xState, zState):
    possible_Win = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8],[0,4,8],[2,4,6]]

    for win in possible_Win:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match")
            return 1
        
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O Won the match")
            return 1
    
    return -1


def checkDraw(xState, zState):
    xCount = 0
    zCount = 0
    
    for i in xState:
        if xState[i] == 1:
            xCount += 1
        
    for j in zState:
        if zState[j] == 1:
            zCount += 1

    if(xCount & zCount == 9):
        print("The game was finished in draw")
        return 1
    
    return -1

#Main function 
if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]

    #it determines the player turn, 1 for X turn and 0 for Y turn
    turn = 1

    print("Welcome to Tic Tac Toe game")

    while(True):
        #print board function call
        printBoard(xState, zState)
        if (turn == 1):
            print("X's chance")
            userInput = int(input("PLease enter a specific value: "))
            xState[userInput] = 1
        else:
            print("O's chance")
            userInput = int(input("PLease enter a specific value: "))
            zState[userInput] = 1

        draw = checkDraw(xState, zState)
        if(draw != -1):
            print("Match is draw")
            break

        #checks the states of both the user to determine whether the game is over or not
        check = checkWin(xState, zState)
        if(check != -1):
            print("Match is over")
            break

       #toggles the turn of the players. 
        turn = 1 - turn
        
    