from renderer import Renderer
import os
import distutils.dir_util

base_dir = os.path.dirname( os.path.realpath( __file__ ) )
c4_dir = os.path.join( base_dir , "c4" )
distutils.dir_util.mkpath( c4_dir )

fen_index = 1

def render_fen( wFEN ):
	global fen_index
	renderer = Renderer()
	surface = renderer.render( wFEN )
	wPath = os.path.join( c4_dir , str( fen_index ) + ".png" )
	print( "Writing to --> " + wPath )
	surface.write_to_png( wPath )
	fen_index = fen_index + 1


def new_fen( wFEN ):
	print( "Rendering New FEN String" )
	print( wFEN )
	render_fen( wFEN )