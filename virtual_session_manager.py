#import ncm_api
import session_manager as manager
import local_stockfish as stockfish
import board_utils
import pprint
import os

pp = pprint.PrettyPrinter( indent=4 )

# c4 - g5 - d4 - white to move
#starting_fen = "rnbqkbnr/pppppp1p/8/6p1/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 1"

# c4 - g5 - d4 - black to move
starting_fen = "rnbqkbnr/pppppp1p/8/6p1/2PP4/8/PP2PPPP/RNBQKBNR b KQkq - 0 1"

batch = board_utils.get_legal_moves_as_fens( starting_fen )

#batch = stockfish.get_best_moves_from_fens( batch )
batch = stockfish.process_batch( batch )

manager.process_batch( batch )