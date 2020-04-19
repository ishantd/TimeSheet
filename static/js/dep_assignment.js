$(".project-info").hide();
$("#hour-assign").hide();
var hours = ""
$('#project').on('change', function() {
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





  