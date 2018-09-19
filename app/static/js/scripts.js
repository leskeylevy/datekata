$(document).ready(function(){
  
  //fixed secondary nav
  
  var secondaryHead = $('nav'),
  secondaryHeadTopPosition = secondaryHead.offset().top;
  $(window).on('scroll', function(){
    if($(window).scrollTop() > secondaryHeadTopPosition ) {
      secondaryHead.addClass('fixed-nav');  
      $(".logo").addClass("fixed-logo");
      $(".logo-title").addClass("fixed-logo");
      $(".logo-box").addClass("fixed-logo-box");
      $("nav ul").addClass("fixed-links");
    } 
    else {
      secondaryHead.removeClass('fixed-nav');
      $(".logo").removeClass("fixed-logo");
      $(".logo-title").removeClass("fixed-logo");
      $(".logo-box").removeClass("fixed-logo-box");
      $("nav ul").removeClass("fixed-links");
    }
  });
  
  //header shrink
  
  var introSection = $('.intro-background'),
  introSectionHeight = introSection.height(),
    //change scaleSpeed if you want to change the speed of the scale effect
  scaleSpeed = 0.4;
    //change opacitySpeed if you want to change the speed of opacity reduction effect
  opacitySpeed = 1; 
  
  $(window).on('scroll', function(){
    window.requestAnimationFrame(animateIntro);
  });
  //assign a scale transformation to the introSection element and reduce its opacity
  function animateIntro () {
    var scrollPercentage = ($(window).scrollTop()/introSectionHeight).toFixed(5),
      scaleValue = 1 - scrollPercentage*scaleSpeed;
    //check if the introSection is still visible
    if( $(window).scrollTop() < introSectionHeight) {
      introSection.css({
        'transform': 'scale(' + scaleValue + ') translateZ(0)',
        'opacity': 1 - scrollPercentage*opacitySpeed
      });
    }
  }
});



// Setting up the Variables
var bars = document.getElementById("nav-action");
var nav = document.getElementById("nav");


//setting up the listener
bars.addEventListener("click", barClicked, false);


//setting up the clicked Effect
function barClicked() {
  bars.classList.toggle('active');
  nav.classList.toggle('visible');
}



