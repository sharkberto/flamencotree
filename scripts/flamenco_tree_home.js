$(document).ready( function() {

	var newdiv = document.createElement( "div" );
	var nodes = jQuery.parseJSON('[{"name":"Tonás"},{"name":"Martinetes"},{"name":"Debla"},{"name":"Pregones"}]');//'[{"name":"Tonás"},{"name":"Martinetes"},{"name":"Debla"},{"name":"Pregones"}]');
	
	$('.explorer').hide();
	
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
		$('.explorer').fadeToggle();
			
     }); 
	
	$('.explorer').hover( 
		function() {
			$(this).addClass('active');
	},
		function() {
			$(this).removeClass('active');
        });

});














