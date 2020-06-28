const deg = 6;
const hr = document.querySelector('#hr')
const mn = document.querySelector('#mn')
const sc = document.querySelector('#sc')

setInterval(()=> {
    let day = new Date();
    let hh = day.getHours() * 30;
    let mm = day.getMinutes() * deg;
    let ss = day.getSeconds() * deg;

    console.log(hh, mm, ss)
    console.log(day)
    
    hr.style.transform = `rotateZ(${(hh)+(mm/12)}deg)`;
    mn.style.transform = `rotateZ(${(mn)}deg)`;
    sc.style.transform = `rotateZ(${(sc)*9}deg)`;
}, 1)


