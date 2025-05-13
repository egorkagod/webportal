function checkFormData(data){
    let errors = []
    if (data.get("password1") !== data.get("password2")){
        errors.push("Пароли не совпадают")
    }
    for (let [key, value] of data.entries()) {
        if (value.trim() === "") {
            errors.push("Пожалуйста, заполните все поля!");
            break;
        }
    }
    if (errors.length > 0){
        return errors
    }
    return false
}

function showErrors(errors){
    let errorDiv = document.getElementById("popup-error")
    errorDiv.innerHTML = errors.join("<br>");
    errorDiv.classList.remove("d-none")
    setTimeout(() => {
        errorDiv.classList.add("d-none");
    }, 3000);
}

async function createUser(data){
    try {
        const response = await fetch("", {
            method: 'POST',
            body: data,
        })

        const result = await response.json()
        if (response.status === 400) {
            showErrors([result.message])
        } else if (response.status === 200) {
            window.location.replace('/');
        } else {
            console.error("Необработан код ответа", response.status)
        }
    } catch (error) {
        console.error('Ошибка при создании пользователя', error)
    }
}

document.getElementById('register-form').addEventListener('submit', async function (e) {
    e.preventDefault()
    const formData = new FormData(this)
    let errors = checkFormData(formData)
    if (errors){
         showErrors(errors)
    } else {
        await createUser(formData)
    }
})