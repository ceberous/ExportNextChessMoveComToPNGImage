from renderer import Renderer
import os
import distutils.dir_util
from collections import defaultdict
import json

fen_index = 1
opening_name = "test"
move_number = 1
move_name = "g5"

base_dir = os.path.dirname( os.path.realpath( __file__ ) )
print( "Base = " + base_dir )
opening_dir = os.path.join( base_dir , opening_name , str( move_number ) )
print( "Opening = " + opening_dir )
move_dir = os.path.join( opening_dir , str( move_name ) )
print( "Move = " + str( move_dir ) )
move_list_json_fp = os.path.join( move_dir , opening_name + "--" + str( move_number ) + "--" + str( move_name ) + ".json" )
distutils.dir_util.mkpath( move_dir )

# Store it in a JSON VoHiYo
saveOBJ = defaultdict( lambda : None )
try:
	with open( savePath ) as f:
		saveOBJ = json.loads( f.read() )
except:
	pass

def render_fen( wFEN ):
	global fen_index

	number_part = str( fen_index )
	if fen_index < 1000:
		number_part = "0" + number_part
	if fen_index < 100:
		number_part = "0" + number_part
	if fen_index < 10:
		number_part = "0" + number_part

	renderer = Renderer()
	surface = renderer.render( wFEN )

	wPath = os.path.join( move_dir , number_part + ".png" )
	print( "Writing to --> " + wPath )
	surface.write_to_png( wPath )
	saveOBJ[ fen_index ] = wFEN
	with open( move_list_json_fp , "w+" ) as outfile:
		json.dump( saveOBJ , outfile )
	fen_index = fen_index + 1
	return fen_index


def new_fen( wFEN ):
	print( "Rendering New FEN String" )
	print( wFEN )
	result = render_fen( wFEN )
	print( "Finished !" )
	return result


def process_batch( batch ):
	#total_fens = str( len( batch[ "moves" ] ) )
	for index , key in enumerate( batch[ "moves" ] ):
		# print( "\n[ " + str( index + 1 ) + " ] of " + total_fens + " " + fen )
		# best_reply = get_best_move_as_fen( fen )
		# batch[ "moves" ][ key ][ "end" ] = best_reply
		render_fen( batch[ "starting_fen" ] )
		render_fen( batch[ "moves" ][ index ][ "start" ] )
		render_fen( batch[ "moves" ][ index ][ "end" ] )
	with open( move_list_json_fp , "w+" ) as outfile:
		json.dump( batch , outfile )
	return batch