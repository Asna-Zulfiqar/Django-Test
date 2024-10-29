const authorBtn = document.getElementById("author-btn");
const userBtn = document.getElementById("user-btn");
const authorForm = document.getElementById("author-form");
const userForm = document.getElementById("user-form");

authorBtn.addEventListener("click", () => {
    authorBtn.classList.add("active");
    userBtn.classList.remove("active");
    authorForm.classList.add("active");
    userForm.classList.remove("active");
});

userBtn.addEventListener("click", () => {
    userBtn.classList.add("active");
    authorBtn.classList.remove("active");
    userForm.classList.add("active");
    authorForm.classList.remove("active");
});
