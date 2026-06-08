console.log("JS成功載入");
const burger = document.querySelector(".burger");
const mobileMenu = document.querySelector(".mobile-menu");
const closeBtn = document.querySelector(".close");

burger.addEventListener("click", () => {
    mobileMenu.classList.add("show");
});

closeBtn.addEventListener("click", () => {
    mobileMenu.classList.remove("show");
});