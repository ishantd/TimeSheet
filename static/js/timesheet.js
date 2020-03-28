$('#submitTS').click(function(){
    event.preventDefault();
    var myform = $("form");
    var disabled = myform.find(':input:disabled').removeAttr('disabled'); // Ser array only takes enabled fields, this is why
    var data = myform.serializeArray();
    disabled.attr('disabled','disabled');
    var employee_id = $('#emp_id').text()
    if (data[0].name == "project") {
        console.log(data[0].value)
    }
    hour_sum = (hours) => {
        var sum=0;
        for (var i=0 ; i<hours.length; i++) {
            sum = hours[i] + sum;
        }
        return sum;
    }
    console.log(data)
    employee_id = parseInt(employee_id.replace('ID: ', ''))
    var ReportData = [];
    var days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    for (var i = 0; i < (data.length+1)/9; i++) {
        var dataObject = {};
        var p_id;
        var activity;
        var hours = [];
        for (var j = i * 9; j < (i+1)*9 ; j++) {
           if(data[j] != undefined) {
            if((j==0 || j%9==0) && data[j].name == "project") {
                if (data[j].value == "Holiday/Leave") {
                    p_id = 0;
                }
                else {
                    p_id = parseInt(data[i].value);
                }
            }
            if(data[j].name == "activity"){
                activity = data[j].value
            }
            if (j > (i*9)+1 && data[j].name.includes("Hours")) {
                hours.push(parseInt(data[j].value)) 
            }
        }
           
        }
        dataObject = {
            Employee_id: employee_id,
            Project_id: p_id,
            Activity: activity,
            Everyday_Hours: hours,
            t_hours: hour_sum(hours),
            time_stamp: Date().toString()
        }
        ReportData.push(dataObject)
    }
    console.log(ReportData)
})