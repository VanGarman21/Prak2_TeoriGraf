def is_valid_move(board, move, n):
    x, y = move
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end="\t")
        print()

def knight_tour(n, start):
    # Inisialisasi papan catur
    board = [[-1 for _ in range(n)] for _ in range(n)]

    # Langkah pertama: Posisi awal
    x, y = start
    board[x][y] = 1

    # Posisi langkah kuda
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Mulai tur kuda
    if knight_tour_util(board, n, start, 2, move_x, move_y):
        print_board(board, n)
    else:
        print("Solusi tidak ditemukan.")

def knight_tour_util(board, n, pos, move_count, move_x, move_y):
    x, y = pos

    # Semua kotak telah dikunjungi
    if move_count == n * n:
        return True

    # Coba semua langkah mungkin
    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        next_move = (next_x, next_y)

        if is_valid_move(board, next_move, n):
            board[next_x][next_y] = move_count

            if knight_tour_util(board, n, next_move, move_count + 1, move_x, move_y):
                return True

            # Backtrack
            board[next_x][next_y] = -1

    return False

# Panggil fungsi knight_tour dengan ukuran papan 8x8 dan posisi awal di a5 
knight_tour(8, (0, 4))
