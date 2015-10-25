$(document).ready( function() {

	var newdiv = document.createElement( "div" );
	var nodes = jQuery.parseJSON('[{"name":"Tonás"},{"name":"Martinetes"},{"name":"Debla"},{"name":"Pregones"}]');//'[{"name":"Tonás"},{"name":"Martinetes"},{"name":"Debla"},{"name":"Pregones"}]');
	
	$('#player').hide();
	
	//HOVER CHANGE COLOR
    $('.palo').hover( 
	  	function(){
			$(this).addClass('active');		
		},
		function() {
			$(this).removeClass('active');
        }
	  );
	  
	$('.palo').click( function(){	
		$("#player").fadeToggle();
		      // 2. This code loads the IFrame Player API code asynchronously.
     }); 
	
	$('.explorer').hover( 
		function() {
			$(this).addClass('active');
	},
		function() {
			$(this).removeClass('active');
        });

});














