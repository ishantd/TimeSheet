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

$(document).on("change", ".saturdayHours_extended", function() {
    var sum = 0;
    $(".saturdayHours_extended").each(function(){
        sum += +$(this).val();
    });
    $("#saturdayTotal_extended").val(sum);
});
$(document).on("change", ".sundayHours_extended", function() {
    var sum = 0;
    $(".sundayHours_extended").each(function(){
        sum += +$(this).val();
    });
    $("#sundayTotal_extended").val(sum);
});
$(document).on("change", ".mondayHours_extended", function() {
    var sum = 0;
    $(".mondayHours_extended").each(function(){
        sum += +$(this).val();
    });
    $("#mondayTotal_extended").val(sum);
});
$(document).on("change", ".tuesdayHours_extended", function() {
    var sum = 0;
    $(".tuesdayHours_extended").each(function(){
        sum += +$(this).val();
    });
    $("#tuesdayTotal_extended").val(sum);
});
$(document).on("change", ".wednesdayHours_extended", function() {
    var sum = 0;
    $(".wednesdayHours_extended").each(function(){
        sum += +$(this).val();
    });
    $("#wednesdayTotal_extended").val(sum);
});
$(document).on("change", ".thursdayHours_extended", function() {
    var sum = 0;
    $(".thursdayHours_extended").each(function(){
        sum += +$(this).val();
    });
    $("#thursdayTotal_extended").val(sum);
});
$(document).on("change", ".fridayHours_extended", function() {
    var sum = 0;
    $(".fridayHours_extended").each(function(){
        sum += +$(this).val();
    });
    $("#fridayTotal_extended").val(sum);
});
