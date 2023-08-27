def create_game_board(rows, cols):
    game_board = [['.' for _ in range(cols)] for _ in range(rows)]
    return game_board

def display_game_board(game_board):
    for row in game_board:
        print(' '.join(row))
        
def main():
    rows = 10
    cols = 20
    game_board = create_game_board(rows, cols)
    
    # Place the snake and ladder on the game board
    game_board[rows - 2][cols // 2] = '#'  # Ladder's position
    game_board[rows - 3][cols // 2] = '#'  # Ladder's position
    game_board[rows - 4][cols // 2] = '#'  # Ladder's position
    game_board[rows - 5][cols // 2] = '#'  # Ladder's position
  # Ladder's position
    
    game_board[4][15] = '#'        # Snake's starting position
    game_board[5][16] = '#'        # Snake's starting position
    game_board[6][17] = '#'        # Snake's starting position
    game_board[7][18] = '#'
    
    game_board[6][5] = '$'        # Snake's starting position
    game_board[5][6] = '$'        # Snake's starting position
    game_board[4][7] = '$'        # Snake's starting position
    game_board[3][8] = '$'        # Snake's starting position
    
    display_game_board(game_board)

if __name__ == "__main__":
    main()
