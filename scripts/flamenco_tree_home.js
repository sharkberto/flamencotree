$(document).ready(function() {

	var curpalo = "placeholder";
	
	//JSON array of palos
	var nodes = jQuery.parseJSON('{"name":"Tonás"}');
  /*{"name":"Martinetes","group":1},
  {"name":"Debla","group":1},
  {"name":"Pregones","group":1}'
  );*/
	
	//TODO:
	// use .append to traverse through tree
	// Once palo children are done, show the songs.
	$().each(nodes, function(i, item) {
		alert(name);
		//create a div for each palo in the json read in
	});	
	// When palo clicked, append divs
    $(".palo").click(function() {
	
        $(".palo").text(function(){
			return curpalo;
		});
		
		//$(".song").toggle();
    });
	
	$(".song").click(function() {
       $(".song").hide();
    }); 

});














