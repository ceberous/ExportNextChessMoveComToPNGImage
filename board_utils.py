# pip2 install 'python-chess==0.23.1' --force-reinstall
import chess
from collections import defaultdict

# https://python-chess.readthedocs.io/en/latest/core.html#moves

def get_legal_moves_as_fens( starting_fen ):
	board = chess.Board( starting_fen )
	legal_moves = list( board.legal_moves )
	#legal_moves.sort()
	legal_fens = []
	continuations = { "starting_fen": starting_fen , "moves": {} }
	for index , move in enumerate( legal_moves ):
		uci_move = move.uci()
		board.push( move )
		new_fen = board.fen()
		#mirror = board.mirror()
		#new_fen = mirror.fen()
		continuations[ "moves" ][ uci_move ] = { "start": new_fen , "end": "" }
		#legal_fens.append( new_fen )
		board.pop()
	#legal_fens.sort()
	#legal_fens.reverse()
	#continuations.reverse()
	#return legal_fens
	keylist = continuations[ "moves" ].keys()
	keylist.sort()
	sortedNew = []
	for index , key in enumerate( keylist ):
		sortedNew.append( { "move": key , "start": continuations[ "moves" ][ key ][ "start" ] , "end": "" } )
		print( "[ " + str( index ) + " ] == " + key + " == " + continuations[ "moves" ][ key ][ "start" ] )
	continuations[ "moves" ] = sortedNew
	return continuations