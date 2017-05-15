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
          overlay.bgcolor = '#76FF03';
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
