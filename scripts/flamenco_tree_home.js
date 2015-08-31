$(document).ready( function() {

	var curpalo = "placeholder";
	var newdiv = document.createElement( "div" );
	var nodes = jQuery.parseJSON('[{"name":"Tonás"},{"name":"Martinetes"},{"name":"Debla"},{"name":"Pregones"}]');//'[{"name":"Tonás"},{"name":"Martinetes"},{"name":"Debla"},{"name":"Pregones"}]');	

    $(".palo").click( function() {
		
		$.each(nodes, function(i, item) {	
		$(".palo").append(item.name); // adjust to create new divs
	});	

    });
	
	$(".song").click(function() {
       $(".song").hide();
    }); 

});














