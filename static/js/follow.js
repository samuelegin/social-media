let followButton = document.querySelectorAll(".followbtn");
let followers = document.querySelectorAll(".followerspan");

for (let i = 0; i < followButton.length; i++) {
    followButton[i].addEventListener("click", () => {
        const id = followButton[i].getAttribute("data-id");
        let status = followButton[i].getAttribute("value");
        if (status === "follow") {
            $.ajax({
                url: "addfollow/",
                method: "POST",
                data: {
                    status: status,
                    id: id
                },
                success: function (data) {
                    followButton[i].innerHTML = "Following";
                    followers[i].innerHTML = `${data.follow_num}`;
                    followButton[i].setAttribute("value", "unfollow");
                }
            });
        } else if (status === "unfollow") {
            $.ajax({
                url: "addfollow/",
                method: "POST",
                data: {
                    status: status,
                    id: id
                },
                success: function (data) {
                    followButton[i].innerHTML = `<i class="bi bi-person-add"></i>`;
                    followers[i].innerHTML = `${data.follow_num}`;
                    followButton[i].setAttribute("value", "follow");
                }
            });
        }
    });
}
