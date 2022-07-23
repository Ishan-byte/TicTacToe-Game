# Imports
from Index import *

# Game class, implmenting OOP concept so that I can 
# seperate the game actual code and main code.
class Game():

    #Overloading sum function that takes three arguments rather than two in the actual super function
    def sum(self,a,b,c):
        return a + b + c

    #Constructor for the Game object that intializes empty set arrays
    def __init__(self, value = None):
        #number of default boxes for the game
        defaultBoxes = 9
        #in case the player inserts his choice of boxes
        if(value != None):
            self.XState = [0] * value
            self.OState = [0] * value
        #default case for the game 
        self.XState = [0] * defaultBoxes
        self.OState = [0] * defaultBoxes

    # method for printing the game board
    # A bit hard coded but will make sure to simplify it as well soon //TODO
    def printBoard(self):
        #hard-coded variables
        indexNames= ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight"]
        indexes = []
        i = 0

        #creating index objects 
        for index in indexNames:
            obj = Index(index)
            indexes.append(obj)   

        #assiging and checking values to the index objects 
        for i in range(i, len(indexes)):
            tmp = 'X' if self.XState[i] else ('O' if self.OState[i] else i)
            indexes[i].setValue(tmp)
            i += 1

        #printing the board
        print("         ")
        print(f"{indexes[0].value} | {indexes[1].value} | {indexes[2].value}")
        print(f"--|---|---")
        print(f"{indexes[3].value} | {indexes[4].value} | {indexes[5].value}")
        print(f"--|---|---")
        print(f"{indexes[6].value} | {indexes[7].value} | {indexes[8].value}")
        print("         ")


    # method for checking whethter the player set has match the wining pattern.
    # It iwll be checked at every turn as it is included in the while loop in the main function
    def checkWin(self):
        possible_Wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]] 
       
        for win in possible_Wins:
            if self.sum(self.XState[win[0]] , self.XState[win[1]] , self.XState[win[2]]) == 3:
                print("X Won damn match")
                return 1

            if (self.sum(self.OState[win[0]] , self.OState[win[1]] , self.OState[win[2]])) == 3:
                print("O Won damn match")
                return 1

        return -1 
    
    # method handles cases where the user inputs unappropriate index numbers
    def indexChecker(self, userInput):
        #Bigger index
        if(userInput > 8):
            print ("This index is way too big! Please choose only those index number that are shown in the boxes.")
            return -1

        # Negative number
        if(userInput < 0):
            print("The index cannot be a negative number.")
            return -1
        
        #Repeated index
        if(self.XState[userInput] == 1) | (self.OState[userInput] == 1):
            print ("This index has already been taken! Please Choose another index.")
            return -1
        
        return 1


    # method that takes the input and class the indexChecker function, basically a manager for user input
    def inputManager(self):
        print("         ")
        userInput = int(input("PLease enter an index value: "))
        while  self.indexChecker(userInput) == -1:
            print("         ")
            userInput = int(input("Please re-enter another value: "))
        return userInput


    # The main method that runs the whole game logic
    def play(self):
        # hard coded variable
        turn = 1
        totalTurn = 0

        print("         ")
        print("Welcome to Tic Tac Toe game")
        
        # iterates till the maximum number of turns for both the players
        while(totalTurn < 9):
            #print board function call
            self.printBoard()

            #turn checker
            if (turn == 1):
                print("X's chance")
                ret = self.inputManager() 
                self.XState[ret] = 1
            else:
                print("O's chance")
                ret = self.inputManager() 
                self.OState[ret] = 1

            #For checking the status of the player sets
            #For Win
            winCheck = self.checkWin()
            if winCheck == 1:
                break

            turn = 1 - turn
            totalTurn += 1

        # in the case that the game has drawn and turn limit have reached 
        if(totalTurn == 9):
            print("The game was drawn")

        # declares the end of match
        print("The Match is over")
