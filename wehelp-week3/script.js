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
let attractionData = [];
let imageMap = {};

let currentIndex = 3;
const cardPerPage = 10;

fetch("https://cwpeng.github.io/test/assignment-3-2")
    .then(function (response) {
        return response.json();
    })
    .then(function (imageData) {

        for (let i = 0; i < imageData.rows.length; i++) {
            let row = imageData.rows[i];
            imageMap[row.serial] = row.pics;
        }

        return fetch("https://cwpeng.github.io/test/assignment-3-1");
    })
    .then(function (response) {
        return response.json();
    })
    .then(function (basicData) {

        attractionData = basicData.rows;

        renderPromotions();
        renderCards();

        document
            .querySelector("#load-more-btn")
            .addEventListener("click", renderCards);
    });

function getFirstImage(serial) {

    let pics = imageMap[serial];

    let firstImage = pics.split(".jpg")[0] + ".jpg";

    return "https://cwpeng.github.io/test" + firstImage;
}

function renderPromotions() {

    const promotions = document.querySelector(".promotions");

    for (let i = 0; i < 3; i++) {

        let attraction = attractionData[i];

        let promotion = document.createElement("div");
        promotion.className = "promotion";

        let img = document.createElement("img");
        img.src = getFirstImage(attraction.serial);

        let span = document.createElement("span");
        span.textContent = attraction.sname;

        promotion.appendChild(img);
        promotion.appendChild(span);

        promotions.appendChild(promotion);
    }
}

function renderCards() {

    const content = document.querySelector(".content");

    let endIndex = currentIndex + cardPerPage;

    for (
        let i = currentIndex;
        i < endIndex && i < attractionData.length;
        i++
    ) {

        let attraction = attractionData[i];

        let card = document.createElement("div");
        card.className = "card";

        let img = document.createElement("img");
        img.src = getFirstImage(attraction.serial);

        let star = document.createElement("div");
        star.className = "star";
        star.textContent = "⭐️";

        let cardText = document.createElement("div");
        cardText.className = "card-text";
        cardText.textContent = attraction.sname;

        card.appendChild(img);
        card.appendChild(star);
        card.appendChild(cardText);

        content.appendChild(card);
    }

    currentIndex = endIndex;

    if (currentIndex >= attractionData.length) {
        document.querySelector("#load-more-btn").style.display = "none";
    }
}