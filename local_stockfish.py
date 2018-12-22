import time
import chess
from pystockfish import *

def get_best_move_as_fen( starting_fen ):
	time1 = time.time()
	#deep = Engine( depth=29 )
	deep = Engine( depth=2 )
	deep.setfenposition( starting_fen )
	result = deep.bestmove()
	next_move = result[ "move" ]

	board = chess.Board( starting_fen )
	uci_move = chess.Move.from_uci( next_move )
	board.push( uci_move )
	new_fen = board.fen()
	#mirror = board.mirror()
	#new_fen = mirror.fen()
	time2 = time.time()
	print '%0.3f seconds == %s' % ( (time2-time1 ) , new_fen )
	return new_fen



def get_best_moves_from_fens( fen_list ):
	time1 = time.time()
	total_fens = str( len( fen_list) )
	replies = []
	for index , fen in enumerate( fen_list ):
		print( "\n[ " + str( index + 1 ) + " ] of " + total_fens + " " + fen )
		best_reply = get_best_move_as_fen( fen )
		replies.append( best_reply )
	time2 = time.time()
	print( "\n" + total_fens  + " FENs Calc Time ==" )
	print '%0.3f seconds' % ( ( (time2-time1 ) ) )
	return replies


def process_batch( batch ):
	time1 = time.time()
	total_fens = str( len( batch[ "moves" ] ) )
	for index , key in enumerate( batch[ "moves" ] ):
		print( "\n[ " + str( index + 1 ) + " ] of " + total_fens + " " + batch[ "moves" ][ index ][ "start" ] )
		best_reply = get_best_move_as_fen( batch[ "moves" ][ index ][ "start" ] )
		batch[ "moves" ][ index ][ "end" ] = best_reply
	time2 = time.time()
	print( "\n" + total_fens  + " FENs Calc Time ==" )
	print '%0.3f seconds' % ( ( ( time2-time1 ) ) )
	return batch