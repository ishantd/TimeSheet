var project = $("#project_id").html();

var dept_data = null;

$.ajax({
    async: false,
    type: 'GET',
    url: '/dept_wise/' + project,
    success: function(data) {
        dept_data = JSON.parse(data);
    }
});



var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
       labels: dept_data.department_names, // responsible for how many bars are gonna show on the chart
       // create 12 datasets, since we have 12 items
       // data[0] = labels[0] (data for first bar - 'Standing costs') | data[1] = labels[1] (data for second bar - 'Running costs')
       // put 0, if there is no data for the particular bar
       datasets: [{
          label: 'Time Allocated',
          data: dept_data.time_allocated,
          backgroundColor: '#22aa99'
       },{
           label: 'Time Reported',
           data: dept_data.time_reported,
           backgroundColor: '#994499'
       }]
    },
    options: {
       responsive: true,
       legend: {
          position: 'right' // place legend on the right side of chart
       },
       scales: {
          xAxes: [{
             stacked: true // this should be set to make the bars stacked
          }],
          yAxes: [{
             stacked: true // this also..
          }]
       }
    }
 });
