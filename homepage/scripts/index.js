$(document).ready(function() {
	// update the time every 1 second
	window.setInterval(function() {
		$('.browser-time').text('The current browser time is ' + new Date() + '.');
	}, 1000);
});