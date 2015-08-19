var fs = require('fs');
var SQL = require('sql.js');
var filebuffer = fs.readFileSync('flamenco_db_v1.sqlite');

// Load the db
var db = new SQL.Database(filebuffer);

// List of tuples, specifying palo and parent indicated by number in the list
var palolabels = ["Bulerías",1];

// Loads palolabels into tree nodes
function loadTree(){

} 

//If palo has no (more) children to show, collapse
function onPaloClick(var palo){

	var boolean hasPaloChildren = false

	if hasPaloChildren == true
	{
	showPaloChildren(palo);
	}
	
		else showPaloSongsFromDB();

}

// shows all sub-styles of the palo
function showPaloChildren(var palo){

}

// Code to load the songs for the palo
function showPaloSongsFromDB(var palo){

// SELECT * FROM db WHERE Palo==?
// For each row returned, generate bubble with caption of letra
// If any duplicates,

}
