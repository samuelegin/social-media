document.addEventListener("DOMContentLoaded", function () {
  const openOthers = document.querySelectorAll(".bi-three-dots-vertical");
  const closeOthers = document.querySelectorAll(".bi-x");
  const others = document.querySelectorAll(".others-div");
  const likeButton = document.querySelectorAll(".bi-heart-fill");
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

  likeButton.addEventListener('click', function () {
    if (isLiked) {
      likeButton.classList.remove('liked');
    } else {
      likeButton.classList.add('liked');
    }

    isLiked = !isLiked;
  });

  const socket = io();
  
  socket.on('connect', () => {
    console.log('Connected to WebSocket');
  });

});
