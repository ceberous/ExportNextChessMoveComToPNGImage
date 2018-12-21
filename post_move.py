import requests
import json
import chess
import personal

# https://curl.trillworks.com/

starting_fen = "rn1qkbnr/p1pppppp/bp6/8/2PPP3/8/PP3PPP/RNBQKBNR w KQkq - 0 1"
print( starting_fen )

headers = {
    'origin': 'https://nextchessmove.com',
    'accept-encoding': 'gzip, deflate, br',
    'x-csrf-token': personal.token ,
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,es;q=0.7',
    'x-requested-with': 'XMLHttpRequest',
    'cookie': personal.cookie ,
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
  ('uuid', personal.uuid ),
]

response = requests.post('https://nextchessmove.com/api/v4/calculate/pro', headers=headers, data=data)
data = json.loads( response.content )

next_move = data[ "move" ]
print( next_move )

board = chess.Board( starting_fen )
uci_move = chess.Move.from_uci( next_move )
board.push( uci_move )
new_fen = board.fen()
print( new_fen )