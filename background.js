$(document).ready(function() {
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
	 	console.log(articles);
	 });
});