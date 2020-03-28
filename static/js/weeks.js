// console.log("TEST")
window.onload = function date() {
    Date.prototype.getWeek = function() {
    var date = new Date(this.getTime());
    date.setHours(0, 0, 0, 0);
    // Thursday in current week decides the year.
    date.setDate(date.getDate() + 3 - (date.getDay() + 6) % 7);
    // January 4 is always in week 1.
    var week1 = new Date(date.getFullYear(), 0, 4);
    // Adjust to Thursday in week 1 and count number of weeks from date to week1.
    return 1 + Math.round(((date.getTime() - week1.getTime()) / 86400000
                          - 3 + (week1.getDay() + 6) % 7) / 7);
  }
  
  // Returns the four-digit year corresponding to the ISO week of the date.
  Date.prototype.getWeekYear = function() {
    var date = new Date(this.getTime());
    date.setDate(date.getDate() + 3 - (date.getDay() + 6) % 7);
    return date.getFullYear();
  }

n =  new Date();
y = n.getFullYear();
m = n.getMonth() + 1;
d = n.getDate();
w = n.getWeek();
// console.log(w)
// document.getElementById("date").innerHTML = d + "/" + m + "/" + y;

var curr = new Date; // get current date
var first = curr.getDate() - curr.getDay(); // First day is the day of the month - the day of the week
// console.log(first)
var last = first + 6; // last day is the first day + 6

var firstday = new Date(curr.setDate(first)).toUTCString().split('2020')[0];
var lastday = new Date(curr.setDate(last)).toUTCString().split('2020')[0];

x = document.getElementById("week").innerHTML = firstday + "-" + lastday
}

days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday" ]
for (var i = 0; i<days.length; i++) {
  
  var x = document.getElementById(days[i])
  var now = new Date;
  var day = now.getDate() - now.getDay(); 
  var y = day + i
  temp = new Date(now.setDate(y));
  y = temp.toUTCString().split('2020')[0]
  x.innerHTML = y
}

var weekString;
var week;
var year;





function getDateOfISOWeek(w, y) {
  var simple = new Date(y, 0, 1 + (w - 1) * 7);
  var dow = simple.getDay();
  var ISOweekStart = simple;
  if (dow <= 4)
      ISOweekStart.setDate(simple.getDate() - simple.getDay() + 1);
  else
      ISOweekStart.setDate(simple.getDate() + 8 - simple.getDay());
  return ISOweekStart;
}

// Returns the ISO week of the date.
Date.prototype.getWeek = function() {
  var date = new Date(this.getTime());
  date.setHours(0, 0, 0, 0);
  // Thursday in current week decides the year.
  date.setDate(date.getDate() + 3 - (date.getDay() + 6) % 7);
  // January 4 is always in week 1.
  var week1 = new Date(date.getFullYear(), 0, 4);
  // Adjust to Thursday in week 1 and count number of weeks from date to week1.
  return 1 + Math.round(((date.getTime() - week1.getTime()) / 86400000 - 3 + (week1.getDay() + 6) % 7) / 7);
}

function getDateRangeOfWeek(weekNo, y){
    var d1, numOfdaysPastSinceLastMonday, rangeIsFrom, rangeIsTo;
    d1 = new Date(''+y+'');
    numOfdaysPastSinceLastMonday = d1.getDay() - 1;
    d1.setDate(d1.getDate() - numOfdaysPastSinceLastMonday);
    d1.setDate(d1.getDate() + (7 * (weekNo - d1.getWeek())));
    rangeIsFrom = (d1.getMonth() + 1) + "-" + d1.getDate() + "-" + d1.getFullYear();
    d1.setDate(d1.getDate() + 6);
    rangeIsTo = (d1.getMonth() + 1) + "-" + d1.getDate() + "-" + d1.getFullYear() ;
    return rangeIsFrom + " to " + rangeIsTo;
};

function getDateByWeek( weeks, year ) {
  var d = new Date(year, 0, 1);
  var dayNum = d.getDay();
  var requiredDate = --weeks * 7;
  // If 1 Jan is Friday to Sunday, go to next week 
  if (((dayNum!=0) || dayNum > 4)) {
      requiredDate += 7;
   }
 // Add required number of days
  d.setDate(1 - d.getDay() + ++requiredDate );
  return d;
}
function getSundayFromWeekNum(weekNum, year) {
  var sunday = new Date(year, 0, (1 + (weekNum - 1) * 7));
  while (sunday.getDay() !== 0) {
      sunday.setDate(sunday.getDate() - 1);
  }
  return sunday;
}

$("#weekButton").click(function(){
  weekString = $("#week").val();
  year = parseInt(weekString.substring(0, 4))
  week = parseInt(weekString.replace(year.toString()+'-W', ''))
  console.log(week, year)
  console.log(getSundayFromWeekNum(week, year)); 
});
