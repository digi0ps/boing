(function(){(function(){(function(){(function(){(function(){function e(e){var t=864e5,n=36e5,r=Math.floor(e/t),i=Math.floor((e-r*t)/n),s=Math.round((e-r*t-i*n)/6e4),o=function(e){return e<10?"0"+e:e};return s===60&&(i++,s=0),i===24&&(r++,i=0),r}var t=new Date(1998,3,6),n=new Date(2017,4,16),r=new Date,i=new Vue({delimiters:["[","]"],el:".days",data:{daysalive:e(r-t),pwning:e(r-n)}});window.sr=ScrollReveal({reset:!0,viewFactor:.1}),sr.reveal(".card")}).call(this)}).call(this)}).call(this)}).call(this)}).call(this);
