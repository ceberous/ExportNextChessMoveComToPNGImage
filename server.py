# sudo pip install git+https://github.com/Pithikos/python-websocket-server
# https://github.com/Pithikos/python-websocket-server
from websocket_server import WebsocketServer

import session_manager as manager

LatestFEN = None

def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	#server.send_message_to_all("Hey all, a new client has joined us")

def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])

def message_received(client, server, message):
	global LatestFEN
	if len( message ) > 200:
		message = message[ :200 ]+ ".."
	#print( "Client(%d) said: %s" % ( client['id'] , message ) )
	if message != LatestFEN:
		LatestFEN = message
		manager.new_fen( LatestFEN )

PORT=9001
server = WebsocketServer( PORT )
server.set_fn_new_client( new_client )
server.set_fn_client_left( client_left )
server.set_fn_message_received( message_received )
server.run_forever()