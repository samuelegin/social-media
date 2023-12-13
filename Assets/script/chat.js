const opened = document.getElementById("bi-comand");
const close = document.getElementById("bi-x");
const liveCircleDiv = document.getElementById("chat-circle");

opened.addEventListener("click", () => {
  liveCircleDiv.style.display = "unset";
});
