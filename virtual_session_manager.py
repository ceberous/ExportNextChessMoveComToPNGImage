import ncm_api
import board_utils
import pprint
pp = pprint.PrettyPrinter(indent=4)

# c4 - g5 - d4 - white to move
#starting_fen = "rnbqkbnr/pppppp1p/8/6p1/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 1"

# c4 - g5 - d4 - black to move
starting_fen = "rnbqkbnr/pppppp1p/8/6p1/2PP4/8/PP2PPPP/RNBQKBNR b KQkq - 0 1"

legal_black_moves = board_utils.get_legal_moves_as_fens( starting_fen )
#pp.pprint( legal_black_moves )

best_white_moves = ncm_api.get_best_moves_from_fens( legal_black_moves )
print( best_white_moves )