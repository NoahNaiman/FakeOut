$(document).ready(function() {
	var http = XMLHttpRequest();
	var url = 'http://localhost:5000/';
	var articles = [];
	 $('*').click(function(e){
		var $target = $(e.currentTarget);
		$target.find('a').each(function(){
			var link = String($(this).attr('href'));
			if(link.indexOf('www.facebook.com') == -1 && link.indexOf('l.facebook.com') == -1 && link != '#' && link.indexOf('http') > -1){
				articles.push(link);
			}
		});
		articles = Array.from(new Set(articles));
//		http.open("POST", url, true);
//		http.setReaquestHeader('Content-type', 'application/x-www-form-urlencoded');
//		http.send(articles);
	 	// var form = document.createElement('form');
	 	// form.method = 'POST';
	 	// form.action = 'http://localhost:5000/';
	 	// form.style.visibility = 'hidden';

	 });
});
