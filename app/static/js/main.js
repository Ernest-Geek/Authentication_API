document.addEventListener('DOMContentLoaded', () => {
    const inputFields = document.querySelectorAll('input[type="text"], input[type="email"], input[type="password"]');
    
    inputFields.forEach(input => {
        input.addEventListener('input', () => {
            input.style.color = '#000'; // White color
        });
    });

    const registerForm = document.getElementById('registerForm');
    const loginForm = document.getElementById('loginForm');

    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(registerForm);
            const data = Object.fromEntries(formData.entries());

            const response = await fetch('/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            window.alert(result.message); // Display registration message as prompt
        });
    }

    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(loginForm);
            const data = Object.fromEntries(formData.entries());

            const response = await fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            document.getElementById('loginResult').textContent = result.message;

            if (response.ok) {
                window.location.href = '/profile/' + result.user_id;
            }
        });
    }
});

const navbarToggleBtn = document.getElementById('navbarToggleBtn');
const navbar = document.getElementById('navbar');

if (navbarToggleBtn && navbar) {
    navbarToggleBtn.addEventListener('click', () => {
        navbar.classList.toggle('show');
    });
}
