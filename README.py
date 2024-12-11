import random

# Mendefinisikan ukuran grid dan jumlah ranjau
GRID_SIZE = 5
NUM_MINES = 5

# Membuat grid permainan yang kosong
def create_board():
    board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    return board

# Menyembunyikan ranjau di dalam grid
def place_mines(board):
    mines = random.sample(range(GRID_SIZE * GRID_SIZE), NUM_MINES)
    for mine in mines:
        row, col = divmod(mine, GRID_SIZE)
        board[row][col] = 'X'

# Menampilkan board
def print_board(board):
    print("  " + " ".join([str(i) for i in range(GRID_SIZE)]))
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))

# Menghitung jumlah ranjau di sekitar sel tertentu
def count_adjacent_mines(board, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    mine_count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE and board[r][c] == 'X':
            mine_count += 1
    return mine_count

# Membuka sel
def open_cell(board, display_board, row, col):
    if board[row][col] == 'X':
        return False
    mine_count = count_adjacent_mines(board, row, col)
    display_board[row][col] = str(mine_count) if mine_count > 0 else ' '
    return True

# Memeriksa apakah pemain sudah menang
def check_win(display_board):
    for row in display_board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def main():
    board = create_board()
    display_board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    place_mines(board)
    
    game_over = False
    while not game_over:
        print_board(display_board)
        
        try:
            row, col = map(int, input("Masukkan baris dan kolom (misal: 1 2): ").split())
            if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
                print("Input tidak valid, coba lagi.")
                continue
        except ValueError:
            print("Input tidak valid, coba lagi.")
            continue
        
        if display_board[row][col] != ' ':
            print("Sel sudah dibuka, pilih sel lain!")
            continue
        
        if not open_cell(board, display_board, row, col):
            print("Game Over! Anda terkena ranjau.")
            print_board(board)
            game_over = True
        elif check_win(display_board):
            print("Selamat! Anda menang.")
            print_board(display_board)
            game_over = True

if __name__ == "__main__":
    main()
# minesweeper
