# pip2 install 'python-chess==0.23.1' --force-reinstall
import chess

# https://python-chess.readthedocs.io/en/latest/core.html#moves
board = chess.Board( "rn1qkbnr/p1pppppp/bp6/8/2PPP3/8/PP3PPP/RNBQKBNR w KQkq - 0 1" )
legal_moves = board.legal_moves

for move in legal_moves:
	print( move )
	board.push( move )
	new_fen = board.fen()
	print( new_fen )
	board.pop()