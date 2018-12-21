# pip2 install 'python-chess==0.23.1' --force-reinstall
import chess

# https://python-chess.readthedocs.io/en/latest/core.html#moves

def get_legal_moves_as_fens( starting_fen ):
	board = chess.Board( starting_fen )
	legal_moves = board.legal_moves
	legal_fens = []
	for move in legal_moves:
		board.push( move )
		new_fen = board.fen()
		legal_fens.append( new_fen )
		board.pop()
	return legal_fens