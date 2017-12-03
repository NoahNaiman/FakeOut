$(document).ready(function() {
	var http = new XMLHttpRequest();
	var url = 'https://localhost:5000/';
	var articles = [];
	var requested = false;
	var i = 0;
	 $('div').click(function(e){
		var $target = $(e.currentTarget);
		$target.find('a').each(function(){
			var link = String($(this).attr('href'));
			if(link.indexOf('www.facebook.com') == -1 && link.indexOf('l.facebook.com') == -1 && link.indexOf('developers.facebook.com') == -1 && link != '#' && link.indexOf('http') > -1 && link != ''){
				if(!requested){
					http.open('POST', url, true);
					http.send(link);
					http.onreadystatechange = function() {
						if(http.readyState == 4 && http.status == 200){
							chrome.runtime.sendMessage({isFakeNews: String(http.responseText)}, function(response) {
								console.log(response.farewell);
							});
						}
					}
					requested = true;
				}
			}
		});
	 });
});