document.addEventListener("DOMContentLoaded", function () {
  const openOthers = document.querySelectorAll(".bi-three-dots-vertical");
  const closeOthers = document.querySelectorAll(".bi-x");
  const others = document.querySelectorAll(".others-div");
  const likeButtons = document.querySelectorAll(".bi-heart-fill");
  let isLiked = false;

  openOthers.forEach((btn, index) => {
    btn.addEventListener("click", function () {
      others[index].style.display = "block";
    });
  });

  closeOthers.forEach((btn, index) => {
    btn.addEventListener("click", function () {
      others[index].style.display = "none";
    });
  });

for (let i = 0; i < likeButtons.length; i++) {
  likeButtons[i].addEventListener('click', function () {
    likeButtons[i].classList.toggle('liked');
  });
}



  
});

