#functions
# Method to print the board in the required format (upside down)
def print_board(board):
    for row in (board):
        print(' '.join(row))


# Method to initialize the board with the specified dimensions
def initialize_board(num_rows, num_cols):
    # Creating a 2D list filled with '-' to represent an empty board
    return [['-'] * num_cols for _ in range(num_rows)]


# Method to insert a chip into the specified column
def insert_chip(board, col, chip_type):
    row = 0
    # Finding the next available spot in the column
    while row < len(board) and board[row][col] == '-':
        row += 1
    # Placing the chip in the available spot or the top if the column is full
    if row > 0:
        board[row - 1][col] = chip_type
    return row - 1  # Returning the row where the chip was placed


# Method to check if the current move results in a win
def check_if_winner(board, col, row, chip_type):
    # Check horizontally for four consecutive chips of the same type
    consecutive_count = 0
    for c in range(len(board[0])):
        if board[row][c] == chip_type:
            consecutive_count += 1
            if consecutive_count == 4:
                return True
        else:
            consecutive_count = 0

    # Check vertically for four consecutive chips of the same type
    consecutive_count = 0
    for r in range(len(board)):
        if board[r][col] == chip_type:
            consecutive_count += 1
            if consecutive_count == 4:
                return True
        else:
            consecutive_count = 0
    return False  # If no winner is found, return False


# Main game logic
def connect_four():
    # Get the dimensions of the board from the user
    num_rows = int(input("What would you like the height of the board to be? "))
    num_cols = int(input("What would you like the length of the board to be? "))

    # Initialize the board and print it
    board = initialize_board(num_rows, num_cols)
    print_board(board)

    # Print the tokens for each player
    print("Player 1: x")
    print("Player 2: o")

    current_player = 1  # Initialize the first player
    while True:
        # Get the current player's information and token type
        player = "Player 1" if current_player == 1 else "Player 2"
        chip_type = 'x' if current_player == 1 else 'o'
        # Get the column input from the current player
        col = int(input(f"{player}: Which column would you like to choose? "))
        # Insert the chip into the chosen column and get the row where it was placed
        row = insert_chip(board, col, chip_type)
        # Print the updated board after the chip is inserted
        print_board(board)
        # Check if the current move results in a win
        if check_if_winner(board, col, row, chip_type):
            print(f"{player} won the game!")
            break
        # Check if the game is a draw if the board is completely filled
        if all(board[i][j] != '-' for i in range(len(board)) for j in range(len(board[0]))):
            print("Draw. Nobody wins.")
            break
        # Switch to the other player's turn
        current_player = 3 - current_player  # Alternating between 1 and 2 for two players

#main
if __name__ == "__main__":
    connect_four()
