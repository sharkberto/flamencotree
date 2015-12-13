$(document).ready( function() {

	var newworkspace = $(".workspace").clone();
	
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
		$('#stop-time').text(formatTime( player.getCurrentTime() ));
		
	}
    });
	
	
	$('#save').submit(function() {
		if ($('#stop-time').not(':empty'))
		{
			//to the right side of player:
			//append start time
			//append end time
			$('#saved').insert("#start-time")
		}
		// add feature div a action="destination_file"...see http://api.jquery.com/submit/

		$('#start-time').empty();
		$('#stop-time').empty();
		return false;
	});
	
	
	function formatTime(time){
		time = Math.round(time);

		var minutes = Math.floor(time / 60),
		seconds = time - minutes * 60;

		seconds = seconds < 10 ? '0' + seconds : seconds;

		return minutes + ":" + seconds;
}

});














