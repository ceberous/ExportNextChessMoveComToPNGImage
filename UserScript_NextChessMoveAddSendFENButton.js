// ==UserScript==
// @name          Next Chess Move Save FEN as PNG image
// @namespace     http://userstyles.org
// @description   Exports nextchessmove.com FEN to python websocket server to generate PNG image
// @author        8932276449
// @include       *://*nextchessmove.com/*
// @run-at        document-start
// @version       0.1
// ==/UserScript==

var ws = undefined;
function init_websocket() {
	try { ws = new WebSocket( "ws://localhost:9001" ); }
	catch( e ) { console.log( "Can't Connect to Python WebSocket" ); }
}

var latest_fen = undefined;
function try_websocket_send() {
	if ( !latest_fen ) { return; }
	try { ws.send( latest_fen ); }
	catch( e ) {
		console.log( "FEN Send Failed , trying to Restart Client" );
		ws = undefined;
		setTimeout( function() {
			init_websocket();
			setTimeout( function() {
				try { ws.send( latest_fen ); }
				catch( e ) { console.log( "Python Websocket Server is Offline" ); }
			} , 500 );
		} , 500 );
	}
}

function getLatestFEN() {
	var links = document.getElementsByTagName( "a" );
	if ( !links ) { return; }
	if ( links.length < 1 ) { return; }

	// No Element ID's or anything so find it
	// 10 everytime so far
	// for ( var i = 0; i < links.length; ++i ) {
	// 	console.log( i.toString() + " == " + links[ i ].innerHTML );
	// }

	if ( !links[ 10 ] ) { return; }
	latest_fen = links[ 10 ].innerHTML;
	if ( latest_fen === "Stockfish 10" ) {
		if ( links[ 12 ] ) {
			latest_fen = links[ 12 ].innerHTML
		}
		else { latest_fen = "error , re-print link order" }
	}

}

function addEventListeners() {
	init_websocket();
	document.body.addEventListener( "keydown" , function( event ) {
		if ( event.key === "Enter" ) {
			getLatestFEN();
			console.log( "sending FEN" );
			console.log( latest_fen );
			try_websocket_send();
			// if ( confirm( "Do you want to post message?" ) === true ) {
			// 	console.log( "passing" );
			// } else {
			// 	event.stopImmediatePropagation();
			// 	event.stopPropagation();
			// 	event.preventDefault();
			// 	return false;
			// }
		}
	});
}

window.addEventListener ( "load" , addEventListeners );

