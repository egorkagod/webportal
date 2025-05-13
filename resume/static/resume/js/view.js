const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content')
const mask = {about: 'Немного и много про себя', profession: 'На кого учился или кем хочешь работать?', education: 'Где учился там и учился', skills: 'Что умеешь?', portfolio: 'Проекты, решения и все все все'}


function showMessage(messages, code, isError=false){
    let componentId = "popup-info"
    if (isError || code >= 400) {
        componentId = "popup-error"
    }
    let component = document.getElementById(componentId)
    component.innerHTML = messages.join("<br>");
    component.classList.remove("d-none")
    setTimeout(() => {
        component.classList.add("d-none");
    }, 3000);
}

const makeObjectEditable = function (event) {
    document.getElementById("updateResume").classList.remove("d-none")
    const component = event.target
    const textarea = document.createElement("textarea")
    textarea.id = component.id
    if (!Object.values(mask).includes(component.textContent)) {
        textarea.value = component.textContent
    }
    textarea.classList.add("big-text")

    component.replaceWith(textarea)
    textarea.focus()

    const replaceBack = function(event) {
        const newComponent = document.createElement(component.tagName)
        newComponent.id = textarea.id
        if (textarea.value === ""){
            newComponent.textContent = mask[textarea.closest("section").id]
        } else {
            newComponent.textContent = textarea.value
        }
        textarea.replaceWith(newComponent)

        newComponent.addEventListener("click", makeObjectEditable)
    }

    textarea.addEventListener("blur", replaceBack)
}

document.querySelectorAll(".editable").forEach(el => {
    el.addEventListener("click", makeObjectEditable)
})

const getResumeData = function (){
    const data = {}
    document.querySelectorAll("#resume > section").forEach(el => {
        const p = el.querySelector("p")
        if (p){
            data[el.id] = p.textContent
        }
    })
    return data
}

document.getElementById("updateResume").addEventListener("click", async function (e) {
    e.preventDefault()
    const data = getResumeData()
    try{
        const response = await fetch("", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken
            },
            body: JSON.stringify(data)
        })
        const result = await response.json()
        if (response.status === 401){
            window.location.href = "/login";
        } else {
            showMessage([result.message], code=response.status)
        }
    } catch (error) {
        console.error("Ошибка при обновлении резюме или обработки ответа", error)
    }
})