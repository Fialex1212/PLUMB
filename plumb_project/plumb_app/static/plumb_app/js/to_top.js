let btnScroll = document.getElementById("to-top");

window.onscroll = function () {
  scrollFunc();
};

function scrollFunc() {
  if (document.body.scroll > 80 || document.documentElement.scrollTop > 80) {
    btnScroll.style.display = "block";
  } else {
    btnScroll.style.display = "none";
  }
}

function toTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}