let hamberMenu = document.getElementById("hamber_btn");
let hamberBody = document.getElementById("hamber_body");

hamberMenu.addEventListener("click", () => {
  if (hamberBody.style.left === "-200px") {
    hamberBody.style.left = "0";
  } else {
    hamberBody.style.left = "-200px";
  }
});