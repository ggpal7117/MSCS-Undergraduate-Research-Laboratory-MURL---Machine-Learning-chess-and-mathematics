# -- Game
# -- Two players pick either 1 or 2 sticks from a pile, and the player to pick up the last stick wins
# -- For simplicity, Max(computer) will go first

# -- Create the min max algorithm based on the amount of sticks there are remaining
def minmax(sticks: int, maxplayer: bool):
    """
    Create an algorithm for the computer to win based off of all possible decisions the human can make
    Input: sticks --> the number of sticks left in the pile. maxplayer --> indicates which player is making a move
    Output: score: int, returns either 1 or -1 to indicate max score to be made by the Max player(computer)
    """
    # -- Base case(Game over) and minplaue(computer) wins
    if sticks == 0 and maxplayer:
        return -1 # --> This means there are no sticks for maxplayer and the minplayer(human) won
    
    # -- Base case(Game over) and maxplayer(computer) wins
    elif sticks == 0 and maxplayer == False:
        return 1
    

    # -- Recursive case max player(computer)
    # -- Recurse through all possilble positions starting with the min players options to bind the best option
    options = [1, 2]

    if maxplayer:
        best_score = float('-inf') # Initialize
        for opt in options:
            if sticks - opt >= 0: # Game still ongoing
                # Call min function on remaing sticks to get an idea of what min(human) will do
                min_score = minmax(sticks-opt, False)
                if min_score > best_score:
                    best_score = min_score # Find best option 
        return best_score

    # -- Recursive case to get all options human can choose(look at the game through humans perspective)
    else:
        best_score = float('inf') # Initialize
        for opt in options:
            if sticks - opt >= 0: # game still ongoing
                # Call max function now
                max_score = minmax(sticks-opt, True)
                if max_score < best_score:
                    best_score = max_score

        return best_score
    

# -- Create additional function to determine which move(1 or 2) produces the highest score
def make_best_move(sticks:int, verbose:bool = False):
    """
    This is a helper function to decide which move is the best for the computer to make
    Input: sticks --> how many sticks are currently at play. Verbose --> if user want to see what the move_scores is
    """
    if verbose:
        print(f"\t----------------------- Algorithm Output-----------------------")
    move_scores = {} # Keep track of scores for each move(1 or 2)
    options = [1, 2]

    for opt in options:
        if sticks - opt >= 0:
            score = minmax(sticks - opt, False)  # AI moves, now it's MIN's turn
            move_scores[opt] = score
            if verbose:
                print(f"\tWhen there are {sticks} sticks, taking {opt} stick(s) results in a score of: {score}")

    best = max(move_scores, key=move_scores.get)
    if verbose:
        print(f"\tBest move for MAX(computer): take {best} stick(s)")
        print(f"\t------------------------------------------------------------")
    return best


# -- Sample game play
def main():
    num_sticks = int(input("Enter a Starting Number of Sticks: "))
    print(f"Lets Play!. There are {num_sticks} sticks")
    verbose_option = input("Would you like to turn on the Verbose Argument ('y/n'): ")

    verbose_option = verbose_option.lower() == 'y'

    # Continue while num_sticks is greater than 0
    while num_sticks > 0:
    # Computer/MAX will make move first
        computer_move = make_best_move(num_sticks, verbose_option)
        num_sticks -= computer_move

        # Check win
        if num_sticks == 0:
            print("There are no more sticks")
            print("The Computer Wins :(")
            break 
        print(f"There are {num_sticks} remaining")
        
        
        user_num = int(input("How Many Sticks Would you Like to Take(1 or 2): "))
        num_sticks -= user_num

        # check win
        if num_sticks == 0:
            print("There are no more sticks")
            print("You win :)")
            break 

        print(f"There are {num_sticks} remaining")


if __name__ == "__main__":
    main()

