const preregister = document.getElementById('preregister')
const option1 = document.getElementById('option1')
const option2 = document.getElementById('option2')
const option3 = document.getElementById('option3')
const option4 = document.getElementById('option4')
const option5 = document.getElementById('option5')
const option6 = document.getElementById('option6')
const option7 = document.getElementById('option7')
const option8 = document.getElementById('option8')

preregister.addEventListener('submit', (e) => {

    if (option1.checked && option4.checked && option5.checked && option7.checked) {
        $('#toRegister').modal('show');
    } else {
        $('#toHome').modal('show');
    }

    e.preventDefault();
})

preregister.addEventListener('click', (e) => {

    if ((option1.checked || option2.checked) && (option3.checked || option4.checked) && (option5.checked || option6.checked) && (option7.checked || option8.checked)) {
        preRegisterBtn.removeAttribute('disabled');
    } else {
        preRegisterBtn.setAttribute('disabled', 'disabled');
    }
})
