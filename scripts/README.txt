YouTube iframe API for Video Control

SIMPLE

1. Load video
2. User sets time range (start and stop time) and adds metadata to describe section
3. Once user clicks the save button next to the comment field, the time range and its comment are saved to cookie/server.
4. A new div is created on submit to enter another range.

SIMPLE 2 (uses OAuth access)

1. Load video based on user query, for example, from user history
2. User labels a clip of the video, by setting the breakpoints, controls (playback quality) and metadata for section
3. Information saved somewhere, to user's youtube account in a cookie?

auth.html
Right now auth not loading because of sameorigin problem? Tried loading from localhost/8000