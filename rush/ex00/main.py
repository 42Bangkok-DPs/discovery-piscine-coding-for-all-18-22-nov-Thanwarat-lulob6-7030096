def is_king_in_check(board):
    def find_king():
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == 'K':
                    return r, c
        return None

    def is_attacked_by_pawn(king_row, king_col):
        directions = [(-1, -1), (-1, 1)]  # Pawn attacks upwards
        for dr, dc in directions:
            nr, nc = king_row + dr, king_col + dc
            if 0 <= nr < size and 0 <= nc < size and board[nr][nc] == 'P':
                return True
        return False

    def is_attacked_in_direction(king_row, king_col, directions, attackers):
        for dr, dc in directions:
            nr, nc = king_row + dr, king_col + dc
            while 0 <= nr < size and 0 <= nc < size:
                if board[nr][nc] == '.':
                    nr += dr
                    nc += dc
                elif board[nr][nc] in attackers:
                    return True
                else:
                    break
        return False

    def is_attacked_by_knight(king_row, king_col):
        knight_moves = [
            (-2, -1), (-2, 1), (2, -1), (2, 1),
            (-1, -2), (-1, 2), (1, -2), (1, 2)
        ]
        for dr, dc in knight_moves:
            nr, nc = king_row + dr, king_col + dc
            if 0 <= nr < size and 0 <= nc < size and board[nr][nc] == 'N':
                return True
        return False

    def is_safe(row, col):
        return not (
            is_attacked_by_pawn(row, col)
            or is_attacked_by_knight(row, col)
            or is_attacked_in_direction(row, col, [(-1, 0), (1, 0), (0, -1), (0, 1)], {'R', 'Q'})
            or is_attacked_in_direction(row, col, [(-1, -1), (-1, 1), (1, -1), (1, 1)], {'B', 'Q'})
        )

    size = len(board)
    king_position = find_king()
    if not king_position:
        print("Error: No King on the board")
        return

    king_row, king_col = king_position

    if not is_safe(king_row, king_col):
        print("Fail")
    else:
        print("The King is safe")

def update_board(board, old_pos, new_pos, piece):
    old_row, old_col = old_pos
    new_row, new_col = new_pos
    board[old_row][old_col] = '.'
    board[new_row][new_col] = piece

if __name__ == "__main__":
    board = [
        ". . . . . . . .",
        ". . . . . . . .",
        ". . P . P . . .",
        ". . . K . . . .",
        ". . . . . . R .",
        ". N . . Q . . .",
        ". . . . . . . .",
        ". . . . . . . ."
    ]

    board = [row.split() for row in board]

    is_king_in_check(board)

    while True:
        print("Enter the piece to move (e.g., K, P, etc.), current position, and new position:")
        print("Example input: K 3 3 2 3 (Move King from row 3, col 3 to row 2, col 3)")
        move = input("Enter move: ").strip().split()
        if len(move) != 5:
            print("Invalid input. Please enter the piece, current position (row, col), and new position (row, col).")
            continue

        piece, old_row, old_col, new_row, new_col = move
        old_row, old_col, new_row, new_col = map(int, [old_row, old_col, new_row, new_col])

        if board[old_row][old_col] != piece:
            print(f"No {piece} found at ({old_row}, {old_col}).")
            continue

        if board[new_row][new_col] != '.':
            print(f"Cannot move to ({new_row}, {new_col}), position is occupied.")
            continue

        update_board(board, (old_row, old_col), (new_row, new_col), piece)
        is_king_in_check(board)
