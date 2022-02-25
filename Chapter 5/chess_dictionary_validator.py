# Automate the Boring Stuff - Chapter 5 Practice Problem

def isValidBoardPosition(position:str) -> bool:
    valid_board_pos = ['1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a',
                       '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b',
                       '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c',
                       '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d',
                       '1e', '2e', '3e', '4e', '5e', '6e', '7e', '8e',
                       '1f', '2f', '3f', '4f', '5f', '6f', '7f', '8f',
                       '1g', '2g', '3g', '4g', '5g', '6g', '7g', '8g',
                       '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h']
    
    if position not in valid_board_pos:
        return False
    
    return True

def isValidChessPiece(piece:str) -> bool:
    valid_chess_pieces = ['wking', 'bking', 'wqueen', 'bqueen', 'wbishop', 'bbishop', 'wknight', 'bknight',
                          'wrook', 'brook', 'wpawn', 'bpawn']
    
    if piece not in valid_chess_pieces:
        return False
    
    return True

def PieceCounts(board:dict) -> dict:
    piece_count = {}

    for v in board.values():
        piece_count[v] = piece_count.get(v, 0) + 1

    return piece_count

def validPieceCount(piece_name:str, count:int) -> bool:
    valid_piece_counts = {'wking': 1, 'bking': 1, 'wqueen': 1, 'bqueen': 1, 'wbishop': 2, 'bbishop': 2, 'wknight': 2, 'bknight': 2,
                          'wrook': 2, 'brook': 2, 'wpawn': 8, 'bpawn': 8}
    
    if count > valid_piece_counts[piece_name]:
        return False

    return True

def isValidChessBoard(board:dict) -> bool:
    piece_totals = PieceCounts(board)

    for k, v in board.items():
        if isValidBoardPosition(k) == False or isValidChessPiece == False:
            return False
    
    for k, v in piece_totals.items():
        if validPieceCount(k, v) == False:
            return False
    
    return True
        
test_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(test_board))