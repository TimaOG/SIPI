const btn = document.querySelector(".btn-toggle");
const theme = document.querySelector("#theme-link");

btn.addEventListener("click", function() {
    if ( document.getElementById("flexSwitchCheckDefault").checked === true ) {
        theme.href = "../static/css/dark_version.css";
    } else {
        theme.href = "../static/css/style.css";
    }
});