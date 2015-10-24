        var channelId;

  // Call the Data API to retrieve information about the currently
  // authenticated user's YouTube channel.
  function getUserChannel() {
    // Also see: https://developers.google.com/youtube/v3/docs/channels/list
    var request = gapi.client.youtube.channels.list({
      // Setting the "mine" request parameter's value to "true" indicates that
      // you want to retrieve the currently authenticated user's channel.
      mine: true,
      part: 'id,contentDetails'
    });

    request.execute(function(response) {
      if ('error' in response) {
        displayMessage(response.error.message);
      } else {
        // We need the channel's channel ID to make calls to the Analytics API.
        // The channel ID value has the form "UCdLFeWKpkLhkguiMZUp8lWA".
        channelId = response.items[0].id;
        // Retrieve the playlist ID that uniquely identifies the playlist of
        // videos uploaded to the authenticated user's channel. This value has
        // the form "UUdLFeWKpkLhkguiMZUp8lWA".
        var uploadsListId = response.items[0].contentDetails.relatedPlaylists.uploads;
        // Use the playlist ID to retrieve the list of uploaded videos.
        getPlaylistItems(uploadsListId);
      }
    });
}
	  
	  // Load the API and make an API call.  Display the results on the screen.
      function loadAPIClientInterfaces() {
        gapi.client.load('youtube', 'v3', function() {
          getUserChannel();
        });
      }