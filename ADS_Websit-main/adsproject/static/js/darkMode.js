document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("themeToggle");
    const themeIcon = document.getElementById("themeIcon");
    const htmlElement = document.documentElement;

    // Define o tema inicial com base no localStorage ou usa "light" como padrão
    const savedTheme = localStorage.getItem("theme") || "light";
    htmlElement.setAttribute("data-bs-theme", savedTheme);
    themeIcon.className = savedTheme === "dark" ? "bi bi-sun-fill" : "bi bi-moon-stars-fill";

    // Alterna o tema ao clicar no botão
    themeToggle.addEventListener("click", function () {
        const currentTheme = htmlElement.getAttribute("data-bs-theme");
        const newTheme = currentTheme === "light" ? "dark" : "light";
        htmlElement.setAttribute("data-bs-theme", newTheme);
        localStorage.setItem("theme", newTheme);
        themeIcon.className = newTheme === "dark" ? "bi bi-sun-fill" : "bi bi-moon-stars-fill";
    });
});