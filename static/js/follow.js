let followButton = document.querySelectorAll(".followbtn");
let unFollowButton = document.querySelectorAll(".unfollowbtn");
let followers = document.querySelectorAll(".followerspan");

for (let i = 0; i < followButton.length; i++) {
    followButton[i].addEventListener("click", () => {
        const id = followButton[i].getAttribute("data-id");
        $.ajax({
            url: "addfollow/",
            method: "POST",
            data: {
                status: "follow",
                id: id
            },
            success: function (data) {
                followButton[i].innerHTML = "UnFollow";
                followers[i].innerHTML = `${data.follow_num}`;
            }
        });
    });
}

for (let j = 0; j < unFollowButton.length; j++)
    unFollowButton[j].addEventListener("click", () => {
        const id = unFollowButton[j].getAttribute("data-id");
        $.ajax({
            url: "addfollow/",
            method: "POST",
            data: {
                status: "unfollow",
                id: id
            },
            success: function (data) {
                unFollowButton[j].innerHTML = "Follow";
                followers[j].innerHTML = `${data.follow_num}`;
            }
        });
    });
