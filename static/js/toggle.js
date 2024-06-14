
const emailInput = document.getElementById('email-input');
const emailError = document.getElementById('email-error');
emailInput.addEventListener('input', function() {
    emailError.style.display = 'none';
    emailInput.classList.remove('is-invalid');
});

document.getElementById('toggle-password').addEventListener('click', function (e) {
    e.preventDefault();
    const passwordInput = document.getElementById('password');
    const eyeIcon = document.getElementById('eye-icon');
    const eyeOffIcon = document.getElementById('eye-off-icon');
    if (passwordInput.getAttribute('type') === 'password') {
        passwordInput.setAttribute('type', 'text');
        eyeIcon.style.display = 'none';
        eyeOffIcon.style.display = 'inline';
        this.title = 'Hide password';
    } 
    else {
        passwordInput.setAttribute('type', 'password');
        eyeIcon.style.display = 'inline';
        eyeOffIcon.style.display = 'none';
        this.title = 'Show password';
    }
});