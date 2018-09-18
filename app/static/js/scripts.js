=================================

/*## NAVBAR PAGE SECTION ##*/

=================================

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



=======================================

/*## 404 ERROR PAGE SECTION ##*/

======================================= 

var lFollowX = 0,
    lFollowY = 0,
    x = 0,
    y = 0,
    friction = 1 / 30;

function animate() {
  x += (lFollowX - x) * friction;
  y += (lFollowY - y) * friction;
  
  translate = 'translate(' + x + 'px, ' + y + 'px) scale(1.1)';

  $('img').css({
    '-webit-transform': translate,
    '-moz-transform': translate,
    'transform': translate
  });

  window.requestAnimationFrame(animate);
}

$(window).on('mousemove click', function(e) {

  var lMouseX = Math.max(-100, Math.min(100, $(window).width() / 2 - e.clientX));
  var lMouseY = Math.max(-100, Math.min(100, $(window).height() / 2 - e.clientY));
  lFollowX = (20 * lMouseX) / 100; // 100 : 12 = lMouxeX : lFollow
  lFollowY = (10 * lMouseY) / 100;

});

animate();



=======================================

/*## 500 INTERNAL SERVER ERROR PAGE SECTION ##*/

======================================= 


Object.assign(document.body.style, {
  color: "#e7852d",
  background: "linear-gradient(to right,#404142,#212326)"
});

const h1 = document.createElement("h1");

Object.assign(h1.style, {
  background: "linear-gradient(to right,#e7852d,#dc124e)",
  "-webkit-background-clip": "text",
  "-webkit-text-fill-color": "transparent",
  fontFamily: "Arial,Helvetica,sans-serif",
  textAlign: "center",
  width: "80%",
  margin: "auto"
});

h1.innerHTML = 'How can a "500 &mdash; Internal Server Error" error happen?';

document.body.appendChild(h1);

setInterval(() => {
  const rand = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;
  const fontFamilies = [
    "Arial Black,Gadget,sans-serif",
    "Impact,Charcoal,sans-serif",
    "Verdana,Geneva,sans-serif",
    "Lucida Console,Monaco,monospace"
  ];
  const fontWeights = ["normal", "bold"];
  const fontStyles = ["normal", "italic", "oblique"];
  const operations = [
    () => {
      const lhs = rand(1, 500);
      const rhs = 500 - lhs;
      return lhs + " + " + rhs + " = " + (lhs + rhs);
    },
    () => {
      const lhs = rand(1, 100);
      const rhs = 500 / lhs;
      return lhs + " * " + rhs + " = " + Math.round(lhs * rhs);
    }
  ];

  const p = document.createElement("p");

  Object.assign(p.style, {
    position: "absolute",
    top: rand(0, document.documentElement.clientHeight) + "px",
    left: rand(0, document.documentElement.clientWidth) + "px",
    fontSize: rand(1, 5) + "em",
    fontFamily: fontFamilies[rand(0, 3)],
    fontWeight: fontWeights[rand(0, 1)],
    fontStyle: fontStyles[rand(0, 2)],
    transform: "rotate(" + rand(-25, 25) + "deg)"
  });

  p.innerHTML = operations[rand(0, 1)]();

  document.body.appendChild(p);

  if (document.body.childNodes.length > 15) {
    document.body.removeChild(document.querySelectorAll("p")[0]);
  }
}, 1000);
