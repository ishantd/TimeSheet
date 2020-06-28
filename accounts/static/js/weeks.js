var weekString;
var week;
var year;

function getBaseUrl() {
  var re = new RegExp(/^.*\//);
  return re.exec(window.location.href);
}

function getSundayFromWeekNum(weekNum, year) {
  var sunday = new Date(year, 0, (1 + (weekNum - 1) * 7));
  while (sunday.getDay() !== 0) {
      sunday.setDate(sunday.getDate() - 1);
  }
  return sunday;
}

function getNumberOfWeek() {
  const today = new Date();
  const firstDayOfYear = new Date(today.getFullYear(), 0, 1);
  const pastDaysOfYear = (today - firstDayOfYear) / 86400000;
  return Math.ceil((pastDaysOfYear + firstDayOfYear.getDay() + 1) / 7);
}


$("#overlay").hide();
$("#selectedWeek").hide();

var cWeek = getNumberOfWeek();

$("#weekButton").click(function(){
  weekString = $("#week").val();
  year = parseInt(weekString.substring(0, 4));
  week = parseInt(weekString.replace(year.toString()+'-W', ''));
  console.log(year, week);
  var weekDone;
  days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday" ];
  $.get("../checkweek/" + week + "/" + year, function(data, status){
    if (data == "no_content") {
      if (week<=cWeek && (cWeek-week)<=9) {
        $("#sWeek").text(weekString);
        $("#chooseWeek").hide();
        $(".check-info").hide();
        $("#overlay").show();
        $("#selectedWeek").show();
        for (var i = 0; i<days.length; i++) {
        var x = document.getElementById(days[i]);
        var now = new Date (getSundayFromWeekNum(week, year));
        var day = now.getDate() - now.getDay(); 
        var y = day + i;
        temp = new Date(now.setDate(y));
        y = temp.toUTCString().split(year.toString())[0];
        x.innerHTML = y;
        }
      }
      else {
        alert("Select week not older than 2 months!");
      }
    }
    else {
      alert("Report of selected week is already submitted.");
    }
  });

});

