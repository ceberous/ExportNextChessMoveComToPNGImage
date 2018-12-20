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
var latest_fen = undefined;
var processing_fen = false;
var send_button = null;

function init_websocket() {
	try { ws = new WebSocket( "ws://localhost:9001" ); }
	catch( e ) { console.log( "Can't Connect to Python WebSocket" ); }
	ws.onmessage = function ( message ) {
		// var x1 = JSON.parse( message.data );
		// if ( !x1 ) { return; }
		if ( message.data === "SUCCESS" ) {
			//send_button.style.backgroundColor = "green";
			send_button.className = "btn btn-xs btn-success";
			send_button.classList.remove( "btn-danger" );
			//send_button.classList.add( "btn-success" );
			send_button.value = "Send FEN";
			processing_fen = false;
			console.log( "READY" );
		}
	};
	ws.onerror = function (error) {
		console.log( "WebSocket error: " + error.toString() );
	};
}

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
	else if ( latest_fen.substring( 0 , 4 ) === "2018" ) {
		if ( links[ 12 ] ) {
			latest_fen = links[ 12 ].innerHTML
		}
		else { latest_fen = "error , re-print link order" }
	}

}


function add_send_button() {
	var calculate_button_parent = document.getElementById( "calculate-button" ).parentElement;
	send_button = document.createElement( "div" );
	send_button.innerHTML = '<button id="send-fen-button" class="btn btn-xs btn-success" style="min-width: 0px;">Send FEN</button>';
	calculate_button_parent.appendChild( send_button );
}

function addEventListeners() {
	init_websocket();
	add_send_button();
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
	document.getElementById( "send-fen-button" ).addEventListener( "click" , function( event ) {
		if ( !processing_fen ) {
			processing_fen = true;
			//send_button.style.backgroundColor = "red";
			send_button.className = "btn btn-xs btn-danger";
			send_button.classList.remove( "btn-success" );
			//send_button.classList.add( "btn-danger" );
			send_button.value = "Processing"
			console.log( "sending FEN !!!" );
			getLatestFEN();
			console.log( latest_fen );
			try_websocket_send();
		}
		else {
			//console.log( "Still Processing , wait" );
			processing_fen = false;
			send_button.className = "btn btn-xs btn-success";
			send_button.classList.remove( "btn-danger" );
			//send_button.classList.add( "btn-success" );
		}
	});
}


window.addEventListener ( "load" , addEventListeners );