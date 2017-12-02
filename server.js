const DataPoint = require('data-point');
const dataPoint = DataPoint.create();

dataPoint.addEntities({
	//remote request of CNN stories
	'request:getCNN':{
		//{value.date} injects value from the accumulator
		url: 'https://services.cnn.com/newsgraph/docs/lastPublishDate:{value.date}'
	}

});
