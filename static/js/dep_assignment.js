$(".project-info").hide();
$("#hour-assign").hide();
var hours = ""
var project;
$('#project').on('change', function() {
    project = parseInt(this.value)
    const sel_id = "#" + (this.value).trim()
    $(sel_id).show();
    $("#hour-assign").show();
    hours = $( sel_id + " .totaltime").text()
    hours = hours.replace("Total Time Assigned: ", "")
    hours = hours.replace(" hours", "")
    hours = parseInt(hours)
    $("#total-hours").val(hours);
  });



$(document).on("change", ".hour-input", function() {
    var sum = 0;
    $(".hour-input").each(function(){
        sum += +$(this).val();
    });
    $("#entered-hours").val(sum);
    $("#left-hours").val(hours - sum)
});

$('#dep_form').submit(function(e){
  e.preventDefault();
  var myform = $("form")
  var data = myform.serializeArray();
  var dept_data = [];
  for (var i=0; i<data.length; i++) {
    var dataObject = {};
    var department_name = data[i].name;
    var time_allocated = parseInt(data[i].value);
    dataObject = {
      department_name: department_name,
      project_assigned: project,
      time_allocated: time_allocated,
      time_left: time_allocated
    }
    dept_data.push(dataObject)
  }
  console.log(dept_data)
});





  