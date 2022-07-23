#Imports
from Game import *

#Running the game // Actual main function
if __name__ == "__main__":
    repeat = 'Y'
    #creating an instance of the GAme object
    testGame = Game()
    #iterates the game until the players says no more
    while (repeat == 'Y') | (repeat == 'y'):
        #Calling the play function that runs the whole game
        testGame.play()
        repeat = input("Do you want to play again? (y/n): ")
    