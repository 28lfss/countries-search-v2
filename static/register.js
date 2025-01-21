const checkUsername = (event) => {
    const usernameFormElement = event.target
    const username = usernameFormElement.value

    axios.post('/auth-user', {
        username: username
    })
    .then((response) => {
        if(response.data.username_exists == 'true') {
            usernameFormElement.setCustomValidity("This user has already been taken!")
        } else {
            usernameFormElement.setCustomValidity("");
        }
        usernameFormElement.reportValidity();
    })
}

const checkEmail = (event) => {
    const emailFormElement = event.target
    const email = emailFormElement.value

    axios.post('/auth-email', {
        email: email
    })
    .then((response) => {
        if(response.data.email_exists == 'true') {
            emailFormElement.setCustomValidity("This email has already been taken!")
        } else {
            emailFormElement.setCustomValidity("");
        }
        emailFormElement.reportValidity();
    })
}
