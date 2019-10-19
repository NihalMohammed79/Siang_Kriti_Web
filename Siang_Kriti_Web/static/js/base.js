// left: 37, up: 38, right: 39, down: 40,
// spacebar: 32, pageup: 33, pagedown: 34, end: 35, home: 36
var keys = { 37: 1, 38: 1, 39: 1, 40: 1 };

function preventDefault(e) {
  e = e || window.event;
  if (e.preventDefault)
    e.preventDefault();
  e.returnValue = false;
}

function preventDefaultForScrollKeys(e) {
  if (keys[e.keyCode]) {
    preventDefault(e);
    return false;
  }
}
function disableScroll() {
  if (window.addEventListener) // older FF
    window.addEventListener('DOMMouseScroll', preventDefault, false);
  window.onwheel = preventDefault; // modern standard
  window.onmousewheel = document.onmousewheel = preventDefault; // older browsers, IE
  window.ontouchmove = preventDefault; // mobile
  document.onkeydown = preventDefaultForScrollKeys;
}

function enableScroll() {
  if (window.removeEventListener)
    window.removeEventListener('DOMMouseScroll', preventDefault, false);
  window.onmousewheel = document.onmousewheel = null;
  window.onwheel = null;
  window.ontouchmove = null;
  document.onkeydown = null;
}
$('#nav-icon3').click(function () {
  $(this).toggleClass('open');
});
$("#nav-icon3").on('click', function () {
  $(".overlay-contentpush,.sidenav,.nav-shift,#fixed-content,body,.nav,.page-content,.svg-background").toggleClass('open');
  if ($(".overlay-contentpush").hasClass("open")) {
    if ($.scrollify != undefined) {
      state = $.scrollify.current().data('section-name');
      $.scrollify.disable();
    }
    disableScroll();
  }
  else {
    enableScroll();
    if ($.scrollify != undefined) {
      $.scrollify.enable();
      $.scrollify.instantMove("#" + state);
    }
  }
})

var can_start = 0;
$(window).on('load',function () {
  $("#lottie").fadeOut();
  $("html").removeClass("init");
  can_start = 1;  
});