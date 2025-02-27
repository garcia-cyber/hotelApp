'use strict';

$(document).ready(function() {

	// Visitors Chart

	if($('#apexcharts-visitors').length > 0) {	
		var options = {
			chart: {
				height: 350,
				type: "area",
				toolbar: {
					show: false
				},
			},
			dataLabels: {
				enabled: false
			},
			stroke: {
				curve: "smooth"
			},
			series: [{
				name: "Income",
				color: '#FFB058',
				data: [45, 60, 75, 51, 42, 42, 30, 10, 8, 22]
			}],
			xaxis: {
				categories: ['18 Nov', '19 Nov', '20 Nov', '21 Nov', '22 Nov', '23 Nov', '24 Nov', '25 Nov', '26 Nov', '27 Nov'],
			}
		}
		var chart = new ApexCharts(
			document.querySelector("#apexcharts-visitors"),
			options
		);
		chart.render();
	}


	// Rooms Booked Chart

	if($('#apexcharts-rooms').length > 0) {	
		var options = {
			series: [44, 55, 67, 83, 57],
			chart: {
				height: 300,
				type: 'radialBar',
		  },
		  plotOptions: {
			radialBar: {
			  dataLabels: {
				show: true,
				value: {
				  fontSize: '30px',
				  color: '#01B8FF'
				},
				total: {
				  show: true,
				}
			  }
			}
		  },
		  labels: ['AC Room', 'Normal Room', 'Video Room', 'Double Bed Room', 'Special Room'],
		  };
  
		  var chart = new ApexCharts(document.querySelector("#apexcharts-rooms"), options);
		  chart.render();
	}

	// Selling Channel Chart

	if($('#apexcharts-selling').length > 0) {	
		var options = {
			series: [{
			name: 'AC ROOM',
			data: [0.4, 0.65, 0.76, 0.88, 1.5, 2.1, 2.9, 3.8]
		  },
		  {
			name: 'NORMAL ROOM',
			data: [-0.8, -1.05, -1.06, -1.18, -1.4, -2.2, -2.85, -3.7]
		  }
		  ],
			chart: {
			type: 'bar',
			height: 285,
			stacked: true,
			toolbar: {
				show: false
			}
		  },
		  colors: ['#0162E8', '#009BDE'],
		  plotOptions: {
			bar: {
			  horizontal: true,
			  barHeight: '60%',
			},
		  },
		  dataLabels: {
			enabled: false
		  },
		  stroke: {
			width: 1,
			colors: ["#fff"]
		  },
		  
		  grid: {
			xaxis: {
			  lines: {
				show: false
			  }
			}
		  },
		  yaxis: {
			title: {
			  // text: 'Age',
			},
		  },
		  toolbar: {
			  show: false,
			  tools: {
				download: false
			  }
		  },
		  tooltip: {
			shared: false,
			x: {
			  formatter: function (val) {
				return val
			  }
			},
			y: {
			  formatter: function (val) {
				return Math.abs(val) + "%"
			  }
			}
		  },
		  title: {
			  show: false
		  },
		  xaxis: {
			categories: ['85+', '80-84', '75-79', '70-74', '65-69', '60-64', '55-59', '50-54'],
			title: {
				show: false,
			},

			labels: {
			  formatter: function (valuesss) {
				return 'Jan'
			  }
			}
		  }
		  };
  
		  var chart = new ApexCharts(document.querySelector("#apexcharts-selling"), options);
		  chart.render();
	}
  
});