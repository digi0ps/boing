(function(){function r(e){var t=864e5,n=36e5,r=Math.floor(e/t),i=Math.floor((e-r*t)/n),s=Math.round((e-r*t-i*n)/6e4),o=function(e){return e<10?"0"+e:e};return s===60&&(i++,s=0),i===24&&(r++,i=0),r}var e=new Date(1998,3,6),t=new Date(2017,4,16),n=new Date,i=new Vue({delimiters:["[","]"],el:".days",data:{daysalive:r(n-e),pwning:r(n-t)}});window.sr=ScrollReveal({reset:!0,viewFactor:.15}),sr.reveal(".card")}).call(this);
