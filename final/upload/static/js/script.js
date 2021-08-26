var slides = document.querySelector(".slides"),
  slide = document.querySelectorAll(".slides li"),
  currentIdx = 0,
  slideCount = slide.length,
  prevBtn = document.querySelector(".prev"),
  slideWidth = 300,
  slideMargin = 30,
  nextBtn = document.querySelector(".next");

slides.style.width =
  (slideWidth + slideMargin) * slideCount - slideMargin + "px";

function moveSlide(num) {
  slides.style.left = -num * 330 + "px";
  currentIdx = num;
}

nextBtn.addEventListener("click", function () {
  if (currentIdx < slideCount - 6) {
    moveSlide(currentIdx + 1);
    console.log(currentIdx);
  } else {
    moveSilde(0);
  }
});

prevBtn.addEventListener("click", function () {
  if (currentIdx > 0) {
    moveSlide(currentIdx - 1);
  } else {
    moveSilde(slideCount - 6);
  }
});

var mvslides = document.querySelector(".mvslides"),
  mvslide = document.querySelectorAll(".mvslides li"),
  mvcurrentIdx = 0,
  mvslideCount = mvslide.length,
  mvprevBtn = document.querySelector(".mvprev"),
  mvslideWidth = 300,
  mvslideMargin = 30,
  mvnextBtn = document.querySelector(".mvnext");

mvslides.style.width =
  (mvslideWidth + mvslideMargin) * mvslideCount - mvslideMargin + "px";

function mvmoveSlide(num) {
  mvslides.style.left = -num * 330 + "px";
  mvcurrentIdx = num;
}

mvnextBtn.addEventListener("click", function () {
  if (mvcurrentIdx < mvslideCount - 6) {
    mvmoveSlide(mvcurrentIdx + 1);
    console.log(mvcurrentIdx);
  } else {
    mvmoveSilde(0);
  }
});

mvprevBtn.addEventListener("click", function () {
  if (mvcurrentIdx > 0) {
    mvmoveSlide(mvcurrentIdx - 1);
  } else {
    mvmoveSilde(mvslideCount - 6);
  }
});


function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

              