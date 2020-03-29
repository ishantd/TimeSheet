$(document).on("change", ".saturdayHours", function() {
    var sum = 0;
    $(".saturdayHours").each(function(){
        sum += +$(this).val();
    });
    $("#saturdayTotal").val(sum);
});
$(document).on("change", ".sundayHours", function() {
    var sum = 0;
    $(".sundayHours").each(function(){
        sum += +$(this).val();
    });
    $("#sundayTotal").val(sum);
});
$(document).on("change", ".mondayHours", function() {
    var sum = 0;
    $(".mondayHours").each(function(){
        sum += +$(this).val();
    });
    $("#mondayTotal").val(sum);
});
$(document).on("change", ".tuesdayHours", function() {
    var sum = 0;
    $(".tuesdayHours").each(function(){
        sum += +$(this).val();
    });
    $("#tuesdayTotal").val(sum);
});
$(document).on("change", ".wednesdayHours", function() {
    var sum = 0;
    $(".wednesdayHours").each(function(){
        sum += +$(this).val();
    });
    $("#wednesdayTotal").val(sum);
});
$(document).on("change", ".thursdayHours", function() {
    var sum = 0;
    $(".thursdayHours").each(function(){
        sum += +$(this).val();
    });
    $("#thursdayTotal").val(sum);
});
$(document).on("change", ".fridayHours", function() {
    var sum = 0;
    $(".fridayHours").each(function(){
        sum += +$(this).val();
    });
    $("#fridayTotal").val(sum);
});
