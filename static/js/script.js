const openOthers = document.getElementsByClassName("bi-three-dots-vertical");
const closeOthers = document.getElementsByClassName("bi-x");
const others = document.getElementsByClassName("others-div");
const posts = document.querySelectorAll(".post-img");
const likes = document.querySelectorAll(".bi-heart-fill");
const likeButton = document.querySelectorAll(".like");
const likeNum = document.querySelectorAll(".likeNum");

for (let i = 0; i < likeButton.length; i++) {
    likeButton[i].addEventListener("click", () => {
        const id = likeButton[i].getAttribute("data-id");
        $.ajax({
            url: "like/",
            data: { id: id },
            method: "POST",
            success: function (data) {
                likeNum[i].innerHTML = data.like;
            }
        });
    });
}

for (let i = 0; i < openOthers.length; i++) {
    openOthers[i].addEventListener("click", function () {
        others[i].style.display = "unset";
    });
}

for (let i = 0; i < closeOthers.length; i++) {
    closeOthers[i].addEventListener("click", function () {
        others[i].style.display = "none";
    });
}

for (let i = 0; i < posts.length; i++) {
    posts[i].addEventListener("dblclick", function () {
        likes[i].style.color = "red";
    });
}
