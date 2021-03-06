var overlay = new Vue({
  delimiters: ["[", "]"],
  el: '.overlay',
  data: {
    message: '',
    bgcolor: '',
    align: '',
    textalign: '',
  }
});

var jargon = new Vue({
  el: '.header',
  methods: {
    changeText: function (dingdong) {
        if(dingdong == 'github') {
          overlay.message = 'Follow my work on GitHub';
          overlay.bgcolor = '#000000';
          overlay.align = 'center';
          overlay.textalign = 'right';
        }
        else if(dingdong == 'uniqna') {
          overlay.message = 'Your university\'s online community';
          overlay.bgcolor = '#FF5722';
          overlay.align = 'center';
          overlay.textalign = 'left';
        }
        else if(dingdong == 'vitcc') {
          overlay.message = 'VIT \'2020';
          overlay.bgcolor = '#283593';
          overlay.align = 'center';
          overlay.textalign = 'center';
        }
        else if(dingdong == 'insta') {
          overlay.message = 'Or instagram?';
          overlay.bgcolor = '#F50057';
          overlay.align = 'center';
          overlay.textalign = 'center';
        }
        else if(dingdong == 'contact') {
          overlay.message = 'Hiring? Here\'s my resume';
          overlay.bgcolor = '#304FFE';
          overlay.align = 'center';
          overlay.textalign = 'center';
        }
        else if(dingdong == 'blog') {
          overlay.message = 'Read my stories and ramblings';
          overlay.bgcolor = '#1ED760';
          overlay.align = 'center';
          overlay.textalign = 'right';
        }
    }
  }
});

$('.button').mouseover(function () {
$('.overlay').show();
}).mouseout(function () {
    $('.overlay').hide();
});

$('.tamil').mouseover(function () {
$('.overlay').show();
}).mouseout(function () {
    $('.overlay').hide();
});

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

window.sr = ScrollReveal({reset: true, viewFactor: 0.05,});
sr.reveal('.scrollText');
