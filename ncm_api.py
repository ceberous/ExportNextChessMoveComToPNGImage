import chess
import requests
import json
import time
import personal

def black_best_move( starting_fen ):
	print( "BestBlackMove()" )
	time1 = time.time()
	headers = {
		'origin': 'https://nextchessmove.com',
		'accept-encoding': 'gzip, deflate, br',
		'x-csrf-token': personal.black_token ,
		'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,es;q=0.7',
		'x-requested-with': 'XMLHttpRequest',
		'cookie': personal.black_cookie ,
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'accept': '*/*',
		'referer': 'https://nextchessmove.com/',
		'authority': 'nextchessmove.com',
		'dnt': '1',
	}

	data = [
	  ('engine', '0f2df4e4afa37946e02a2b647ff21146e0588af7'),
	  ('fen',  starting_fen ),
	  ('position[fen]', starting_fen ),
	  ('movetime', '15'),
	  ('syzygy', 'true'),
	  ('uuid', personal.black_uuid ),
	]

	response = requests.post('https://nextchessmove.com/api/v4/calculate/pro', headers=headers, data=data)
	data = json.loads( response.content )
	next_move = data[ "move" ]
	if next_move is None:
		print( data[ "comment" ] )
		return data[ "comment" ]

	board = chess.Board( starting_fen )
	uci_move = chess.Move.from_uci( next_move )
	board.push( uci_move )
	new_fen = board.fen()
	time2 = time.time()
	print '%0.3f seconds == BLACK == %s' % ( (time2-time1 ) , new_fen )
	return new_fen


def white_best_move( starting_fen ):
	print( "BestWhiteMove()" )
	time1 = time.time()
	headers = {
			'origin': 'https://nextchessmove.com',
			'accept-encoding': 'gzip, deflate, br',
			'x-csrf-token': personal.white_token ,
			'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,es;q=0.7',
			'x-requested-with': 'XMLHttpRequest',
			'cookie': personal.white_cookie ,
			'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'accept': '*/*',
			'referer': 'https://nextchessmove.com/',
			'authority': 'nextchessmove.com',
			'dnt': '1',
	}

	data = {
		'engine': '0f2df4e4afa37946e02a2b647ff21146e0588af7',
		'fen': starting_fen ,
		'position[fen]': starting_fen ,
		'movetime': '15',
		'syzygy': 'true',
		'uuid': personal.white_uuid
	}

	response = requests.post('https://nextchessmove.com/api/v4/calculate/pro', headers=headers, data=data)
	data = json.loads( response.content )
	next_move = data[ "move" ]
	if next_move is None:
		print( data[ "comment" ] )
		return data[ "comment" ]

	board = chess.Board( starting_fen )
	uci_move = chess.Move.from_uci( next_move )
	board.push( uci_move )
	new_fen = board.fen()
	time2 = time.time()
	print '%0.3f seconds == WHITE == %s' % ( (time2-time1 ) , new_fen )
	return new_fen


def get_best_moves_from_fens( fen_list ):
	time1 = time.time()
	total_fens = str( len( fen_list) )
	replies = []
	for index , fen in enumerate( fen_list ):
		print( "\n[ " + str( index + 1 ) + " ] of " + total_fens + " " + fen )
		fen_parts = fen.split()
		if fen_parts[ 1 ] == "b":
			best_reply = black_best_move( fen )
		elif fen_parts[ 1 ] == "w":
			best_reply = white_best_move( fen )
		else:
			pass
		replies.append( best_reply )
	time2 = time.time()
	print( "\n" + total_fens  + " FENs Calc Time ==" )
	print '%0.3f seconds' % ( ( (time2-time1 ) ) )
	return replies


#get_best_moves_from_fens( [ "rnbqkbnr/pppppp1p/8/6p1/2PP4/8/PP2PPPP/RNBQKBNR b KQkq - 0 1" , "rnbqkbnr/pppppp1p/8/6p1/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 1" ] )


#get_best_moves_from_fens( [ "rnbqkb1r/pppppp1p/7n/6p1/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 1 2" ] )