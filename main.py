import random

# Constant value to have max lines in slot machines
MAX_LINES = 3 
# Constants to have a max and min bet amount
MAX_BET = 100
MIN_BET = 1

'''
For the purpose of this project the slot machine will be a 3x3 reel matrix and the user will win if they get 3 in a row
'''
ROWS = 3
COLS = 3

'''
Create a dictionary for the amount of symbols in each reel (A is the most rare)
It may not be the most balanced slot machine, but for the sake of simplicity in this project this will do
'''
symbolCount = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbolValue = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Method to check whether or not the user won
def checkWinnings(columns, lines, bet, values):
    winnings = 0
    winningLines = []
    # Go through each line depending how many lines the user bet on
    for line in range(lines):
        # Grab the first symbol of the row in the first column
        symbol = columns[0][line]
        # Go through each symbol  in the row
        # If the symbol to check does not equal the first symbol in the row, break
        for column in columns:
            symbolCheck = column[line]
            if symbol != symbolCheck:
                break
        else:
            # If all symbols in the row are the same, add the winnings along with adding which line the user won on
            winnings += values[symbol] * bet
            winningLines.append(line + 1)
    
    return winnings, winningLines

# Function which determines what is the output of the spin
def getSlotMachineSpin(rows, cols, symbols):
    allSymbols = []
    # Iterate through dictionary to add into list
    for symbol, symbolCount in symbols.items():
        # For loop which loops through the symbolCount so we can add the specified amount of letters
        for _ in range(symbolCount):
            allSymbols.append(symbol)

    columns = []

    #  generate a column for each column the slot machine has
    for _ in range(cols):
        column = []
        # Copy symbols (not refernece) array so that we don't have any duplicates
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            # Randomly generate a symbol for each section of the row
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns


# Method which will cleanly print the slot machine
def printSlotMachine(columns):
    # Loop through all of the columns 
    for row in range(len(columns[0])):
        # Enumerate to access the current index to print a sepration
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                # Use the end keyword to ensure the next print statement doesn't end up on a new line
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        # Prints the first row and ensures all characters in the first row are in the same line
        print()

# Function which deposits money from the user
def deposit():
    # While loop to continuously ask user for input until something else is pressed
    while True:
        # Ask the user for input by asking how much they want to deposit
        amount = input("How much to deposit? $:")

        # Check if user input is a valid number
        if amount.isdigit():
            #  Convert input into an int and check if it is greater than 0
             amount = int(amount)
             if amount  > 0:
                 break
             else:
                 print("Printed amount me a positive number greater than 0")
        else:
            print("Input an actual number")

    # Once user inputs a valid amount to deposit, return amount
    return amount

# Method to ask the user how many lines in the slot machine they want to bet on (Max: 3)
def getNumberOfLines():
    while True:
        # Ask the user how many lines they want to spin on and check if it falls withing 1-3 inclusively
        lines = input("How many lines do you want to spin on? (1- " + str(MAX_LINES) + ") :")

        if lines.isdigit():
             lines = int(lines)
             if lines <= MAX_LINES and lines >= 1:
                 break
             else:
                 print("Pick the amount of lines between 1-3")
        else:
            print("Input an actual number")

    return lines

# Function which will ask the user how much they want to bet
def getBet():
    # Ask the user how much they want to bet and ensure it is a valid number and falls within the min and max bet
    while True:
        betAmount = input("How much do you want to bet on each line? (MIN: " + str(MIN_BET) + " MAX: " + str(MAX_BET) + "):")
        if betAmount.isdigit():
             betAmount = int(betAmount)
             if MIN_BET <= betAmount <= MAX_BET:
                 break
             else:
                 print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Input an actual number")

    return betAmount

# Method to start the game
def spinMachine(balance):
    lines = getNumberOfLines()
    # Ensure that the amount of bet is within the user's balance
    while True:
        bet = getBet()
        totalBet = bet * lines

        if totalBet > balance:
            print(f"The total bet exceeds your balance (Current Balance: ${balance})")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. \nTotal bet on all lines: ${totalBet}")
    # Call function to get the users spin
    slot = getSlotMachineSpin(ROWS, COLS, symbolCount)
    # Print result of the spin
    printSlotMachine(slot)
    # Check how much the user won and print their winnings
    winnings, winningLines = checkWinnings(slot, lines, bet, symbolValue)
    print(f"You won: ${winnings}")
    '''
    Splat operater (unpack operator) (*)
    This will unpack every value of the list
    '''
    print(f"You won on lines: ", *winningLines)

    return winnings - totalBet

# Main function to start program
def main():
    # Call function to start program
    balance = deposit()
    # While loop so the user can keep spinning if they desire
    while True:
        print(f"Your Balance is: ${balance}")
        ans = input("Press enter to start playing or 1 to quit to leave the machine")

        # Stop the game if the user's balance reaches a negative price
        if balance < 0:
            print("You are below a positive balance, please come back later.")
            break

        if ans == "1":
            break
        balance += spinMachine(balance)

    print(f"The money you left with is: ${balance}")
main()