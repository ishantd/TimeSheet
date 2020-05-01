$("#selectEmployee").hide();

$('#project').on('change', function() {
    $("#selectEmployee").show();
  });

  $('#emp_form').submit(function(e){
    e.preventDefault();
    var myform = $("form")
    var data = myform.serializeArray();
    var employee_list = [];
    var project;
    var dataObject = {};
    for (var i = 0; i < data.length; i++) {
      if (data[i].name == "project" && data[i].value != ""){
        project = data[i].value;
      }
      if (data[i].name == "employee") {
        employee_list.push(parseInt(data[i].value));
      }
    }
    emp_string = employee_list.join();
    dataObject = {
      project: project,
      employees: emp_string
    };
    $.post("/selectEmp/", dataObject, function(){
      console.log("Bool");
    });
  });