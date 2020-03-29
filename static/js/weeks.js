var weekString;
var week;
var year;

function getSundayFromWeekNum(weekNum, year) {
  var sunday = new Date(year, 0, (1 + (weekNum - 1) * 7));
  while (sunday.getDay() !== 0) {
      sunday.setDate(sunday.getDate() - 1);
  }
  return sunday;
}

$("#overlay").hide()

$("#weekButton").click(function(){
  weekString = $("#week").val();
  year = parseInt(weekString.substring(0, 4))
  week = parseInt(weekString.replace(year.toString()+'-W', ''))
  days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday" ]
  $(".check-info").hide()
  $("#overlay").show()
  for (var i = 0; i<days.length; i++) {
  var x = document.getElementById(days[i])
  var now = new Date (getSundayFromWeekNum(week, year))
  var day = now.getDate() - now.getDay(); 
  var y = day + i
  temp = new Date(now.setDate(y));
  y = temp.toUTCString().split(year.toString())[0]
  // console.log(y)
  x.innerHTML = y
}
});

