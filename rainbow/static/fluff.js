var alpha = new Date(1998, 03, 06);
var nf = new Date(2017, 04, 16);
var present = new Date();

function milli2days(t){
    var cd = 24 * 60 * 60 * 1000,
        ch = 60 * 60 * 1000,
        d = Math.floor(t / cd),
        h = Math.floor( (t - d * cd) / ch),
        m = Math.round( (t - d * cd - h * ch) / 60000),
        pad = function(n){ return n < 10 ? '0' + n : n; };
  if( m === 60 ){
    h++;
    m = 0;
  }
  if( h === 24 ){
    d++;
    h = 0;
  }
  return d;
}

var daysalive  = new Vue({
  delimiters: ["[", "]"],
  el: '.days',
  data: {
    daysalive: milli2days(present - alpha),
    pwning: milli2days(present - nf)
  }
});

window.sr = ScrollReveal({reset: true, viewFactor: 0.15,});
sr.reveal('.card');
