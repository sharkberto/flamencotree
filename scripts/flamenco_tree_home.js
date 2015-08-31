$(document).ready(function() {

	var curpalo = "placeholder";
	
	var nodes = jQuery.parseJSON('[{"name":"Tonás"},{"name":"Martinetes"},{"name":"Debla"},{"name":"Pregones"}]');
	
	//TODO:
	// use .append to traverse through tree
	// Once palo children are done, show the songs.
	$().each(nodes, function(i, item) {
		$("div").append(name);
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














