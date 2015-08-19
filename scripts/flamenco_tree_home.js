

$(document).ready(function() {
	var fs = require('fs');
	var SQL = require('sql.js');
	var filebuffer = fs.readFileSync('flamenco_db_v1.sqlite');

	var result = db.exec("SELECT Artist FROM flamenco_table_v1 WHERE id=2");
	console.log(result);
	
	$(".song").hide();
    $(".palo").click(function() {
        //$(".palo").fadeOut('slow',0);
		$(".song").toggle();
    });
	
	 $(".song").click(function() {
        $(".song").hide();
    }); 
});















