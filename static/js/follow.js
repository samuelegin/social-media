let followButton = document.getElementById("follow");
let unFollowButton = document.getElementById("unfollow");

followButton.addEventListener("click",() => {
  $.ajax({
    url:"{% url 'post:addfollow' follow.id %}",
    method:"POST",
    data:{"status":"follow"},
    success: function (data){
      console.log(data)
    }
  })
})
unFollowButton.addEventListener("click",() => {
  $.ajax({
    url:"{% url 'post:addfollow' follow.id %}",
    method:"POST",
    data:{"status":"unfollow"},
    success: function (data){
      console.log(data)
    }
  })
})
