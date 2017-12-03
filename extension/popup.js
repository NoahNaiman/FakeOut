chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse){
  	var alerts = false;
  	var options = {
	  type: "basic",
	  title: "FAKE NEWS DETECTED",
	  message: "Stop the spread! Read carefully selected articles and become more knowledgable.",
	  iconUrl: "icon128.png" 
	}
	chrome.notifications.create("fakeNews", options, function(){
		chrome.browserAction.setBadgeText({text:"!"});
	});

    if(request.isFakeNews == "FAKE"){
    	var alerts = true;
    	sendResponse({farewell: "FAKE NEWS"});
    	chrome.browserAction.setBadgeText({text:"!"});
    	document.getElementById('firstText').innerHTML = 'This Article Is Fake News';
    }
    else{
    	sendResponse({farewell: "REAL NEWS"});
    	document.getElementById('firstText').textContent="Good News";
    }
  });

chrome.browserAction.onClicked.addListener(function(tab) {
    chrome.browserAction.setBadgeText({
	    'text': '' //an empty string displays nothing!
	});
});