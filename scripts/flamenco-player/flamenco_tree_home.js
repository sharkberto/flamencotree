$(document).ready( function() {

	var newtime = document.createElement("div");
	newtime.innerHTML = "Hello";
	var nodes = jQuery.parseJSON('[{"name":"Tonás"},{"name":"Martinetes"},{"name":"Debla"},{"name":"Pregones"}]');//'[{"name":"Tonás"},{"name":"Martinetes"},{"name":"Debla"},{"name":"Pregones"}]');
	
	//$('#player').hide();
	
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
	 
	 //When logging a video event like a guitar solo, use button to call player.getCurrentTime():Number
	 //Same button to save the time the video event ends
	 //Save these two times with the video ID and a user generated label
	
	
	$('.explorer').hover( 
		function() {
			$(this).addClass('active');
	},
		function() {
			$(this).removeClass('active');
        });
		
	$('#addtime').click(function() {
		
		if ($('#start-time').is(':empty')) {
		// do something
		$('#start-time').text(formatTime( player.getCurrentTime() ));
		
		} else {
		$('#end-time').text(formatTime( player.getCurrentTime() ));
		
	}
    });
	
	
	$('#save').click(function saveFeature() {
	document.body.appendChild(newtime);
/* 		$('#feature').submit(function () {
		
		return false; 
		});*/
		
		// give feature div a action="destination_file"...see http://api.jquery.com/submit/
		//send start and end times to this file as well
		//add information to a list that displays at right of video
		
	
	
	});
	
	function formatTime(time){
		time = Math.round(time);

		var minutes = Math.floor(time / 60),
		seconds = time - minutes * 60;

		seconds = seconds < 10 ? '0' + seconds : seconds;

		return minutes + ":" + seconds;
}

});














