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



var ctx = document.getElementById('department_bar').getContext('2d');
var act_pie = document.getElementById('activity_pie');


var chart = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
       labels: dept_data.department_names, 
       datasets: [{
          label: 'Controlled Manhours Left',
          data: dept_data.time_allocated,
          backgroundColor: '#22aa99'
       },{
           label: 'Controlled Manhours Reported',
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

var act_data = null;

$.ajax({
    async: false,
    type: 'GET',
    url: '/act_wise/' + project,
    success: function(data) {
        act_data = JSON.parse(data);
    }
});

new Chart(act_pie, {
    type: 'doughnut',
    data: {
      labels: act_data.activity_names,
      datasets: [
        {
          label: "Time spent per activity",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          data: act_data.activity_time
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Activity Wise Time Distribution for Project'
      }
    }
});
