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

function submitAuthentication(event) {
    event.preventDefault()
    checkUsername(event)
    checkEmail(event)
}

const clearUsernameValidity = () => {
    const usernameFormElement = document.getElementById("username");
    usernameFormElement.setCustomValidity("");
    usernameFormElement.reportValidity();
};

const clearEmailValidity = () => {
    const emailFormElement = document.getElementById("email");
    emailFormElement.setCustomValidity("");
    emailFormElement.reportValidity();
};

document.getElementById("username").addEventListener("input", clearUsernameValidity);
document.getElementById("email").addEventListener("input", clearEmailValidity);