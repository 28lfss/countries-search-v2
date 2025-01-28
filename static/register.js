const checkUsername = (event) => {
    event.preventDefault()

    const usernameFormElement = document.getElementById("username")
    const username = usernameFormElement.value

    axios.post('/auth-user', {
        username: username
    })
    .then((response) => {
        if(response.data.username_exists === 'true') {
            usernameFormElement.setCustomValidity("This user has already been taken!")
        } else {
            usernameFormElement.setCustomValidity("");
        }
        usernameFormElement.reportValidity();
    })
}

const checkEmail = (event) => {
    event.preventDefault()

    const emailFormElement = document.getElementById("email")
    const email = emailFormElement.value

    axios.post('/auth-email', {
        email: email
    })
    .then((response) => {
        if(response.data.email_exists === 'true') {
            emailFormElement.setCustomValidity("This email has already been taken!")
        } else {
            emailFormElement.setCustomValidity("");
        }
        emailFormElement.reportValidity();
    })
}

const checkPasswords = (event) => {
    event.preventDefault()

    const passwordFormElement = document.getElementById("password")
    const password = passwordFormElement.value
    const confirmPasswordFormElement = document.getElementById("confirm_password")
    const confirmPassword = confirmPasswordFormElement.value

    if (password === confirmPassword) {
        confirmPasswordFormElement.setCustomValidity("")
    } else {
        confirmPasswordFormElement.setCustomValidity("Passwords must match");
    }

    confirmPasswordFormElement.reportValidity();
}

function submitAuthentication(event) {
    event.preventDefault()
    checkUsername(event)
    checkEmail(event)
    checkPasswords(event)
}

const clearValidity = (elementId) => {
    const formElement = document.getElementById(elementId);
    formElement.setCustomValidity("");
    formElement.reportValidity();

};

["username", "email", "confirm_password"].forEach((id) => {
    document.getElementById(id).addEventListener("input", () => clearValidity(id));
});
