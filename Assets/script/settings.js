let logoutBtn = document.querySelector(".log-out");
let logoutPrompt = document.querySelector(".logout-prompt");
const noBtn = document.querySelector(".no")
let body = document.body;

logoutBtn.addEventListener("click", () => {
    logoutPrompt.style.display = "unset";
    body.classList.add("blur-background");
});

noBtn.addEventListener("click",()=>{
    logoutPrompt.style.display = "none";
})
