$(document).ready( function() {

	var newdiv = document.createElement( "div" );
	var nodes = jQuery.parseJSON('[{"name":"Tonás"},{"name":"Martinetes"},{"name":"Debla"},{"name":"Pregones"}]');//'[{"name":"Tonás"},{"name":"Martinetes"},{"name":"Debla"},{"name":"Pregones"}]');
	
	$('#player').hide();
	
    $('.palo').hover( 
	  	function(){
			$(this).addClass('active');
				/*
				$.each(nodes, function(i, item) {	
				$(".palo").append(item.name); // adjust to create new divs
				*/
				
		},
		function() {
			$(this).removeClass('active');
        }
	  );
	  
	$('.palo').click( function(){
			
		$("#player").fadeToggle();
		      // 2. This code loads the IFrame Player API code asynchronously.
/*       $.getScript("player-control.js", function(){
    alert("Running player-control.js");
		}); */

			
     }); 
	
	$('.explorer').hover( 
		function() {
			$(this).addClass('active');
	},
		function() {
			$(this).removeClass('active');
        });

});














