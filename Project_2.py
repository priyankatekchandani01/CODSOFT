# TIC-TAC-TOE AI
#  Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player. You can use 
#  algorithms like Minimax with or without Alpha-Beta Pruning to make the AI player unbeatable.
#  This project will help you understand game theory and basic search algorithms

def print_board(board):
    print("\n")
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print("|".join(row))
        if i<2:
            print("-"*5)
    print("\n")

def check_winner(board,player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False
    
def check_draw(board):
    return " " not in board

def available_moves(board):
    available = []

    for i,spot in enumerate(board):
        if spot == " ":
            available.append(i)
    return available

def minimax(board,is_maximizing):
    if check_winner(board,"O"):
        return 1
    elif check_winner(board,"X"):
        return -1
    elif check_draw(board):
        return 0
    
    if is_maximizing:
        best_score = -1000
        for i in available_moves(board):
            board[i] = "O"
            score = minimax(board,False)
            board[i] = " "
            best_score = max(score,best_score)
        return best_score
    else:
        best_score = 1000
        for i in available_moves(board):
            board[i] = "X"
            score = minimax(board,True)
            board[i] = " "
            best_score = min(score,best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None

    for i in available_moves(board):
        board[i] = "O"
        score = minimax(board,False)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    return move

def play_game():
    board = [" " for _ in range(9)]
    print("Welcome to Tic-Tac-Toe")
    print("You are X.AI is O.")
    print("Enter positions from 0 to 8 as shown below: ")
    print("0 | 1 | 2\n----------\n3 | 4 | 5\n----------\n6 | 7 | 8")

    while True:
        print_board(board)

        try:
            move = int(input("Enter Move: "))
        except:
            print("Enter a valid number")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid Move. Try Again.")
            continue
        board[move] = "X"

        if check_winner(board,"X"):
            print_board(board)
            print("You win!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw")
            break

        ai = best_move(board)
        board[ai] = "O"
        print(f"AI choose position {ai}") 

        if check_winner(board,"O"):
            print_board(board)
            print("AI wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw")
            break

play_game()
