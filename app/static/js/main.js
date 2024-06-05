document.addEventListener('DOMContentLoaded', () => {
    const inputFields = document.querySelectorAll('input[type="text"], input[type="email"], input[type="password"]');
    
    inputFields.forEach(input => {
        input.addEventListener('input', () => {
            input.style.color = '#ffc107'; // Change text color to yellow
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
            document.getElementById('registerResult').textContent = result.message;
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
