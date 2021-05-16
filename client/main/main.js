const toggleBtn = document.querySelector('.mainbar_toggleBtn');
const menu = document.querySelector('.main_menu');
const login = document.querySelector('.main_button');

toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
    login.classList.toggle('active');
});