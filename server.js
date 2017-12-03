var PythonShell = require('python-shell');

var options = {
  mode: 'text',
  pythonPath: '/usr/bin/python',
  pythonOptions: ['-u'],
  scriptPath: '.',
};

var shell = new PythonShell('data.py', options, {
    mode: 'text'
});

shell.stdout.on('data', function (message) {
	if (message == '[READY]') {
		shell.send('go\n').end(function(err){
		    if (err) handleError(err);
		    else ;
		});
	}
		/*shell.send('hi!').end(function(err){
			if (err) console.error(err);
		});*/
	console.log(message);
});

shell.end(function(err) {
    if (err) throw err;
    console.log('End Script');
});



