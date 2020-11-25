const preregister = document.getElementById('preregister')
const option1 = document.getElementById('option1')
const option2 = document.getElementById('option2')
const option3 = document.getElementById('option3')
const option4 = document.getElementById('option4')



preregister.addEventListener('submit', (e) => {

    if (option1.checked && option4.checked) {
        $('#toRegister').modal('show');
    } else {
        $('#toHome').modal('show');
    }

    e.preventDefault();
})

preregister.addEventListener('click', (e) => {


    if ((option1.checked || option2.checked) && (option3.checked || option4.checked) ) {
        preRegisterBtn.removeAttribute('disabled');
    } else {
        preRegisterBtn.setAttribute('disabled', 'disabled');
    }
})

    // preRegisterBtn.setAttribute('disabled','disabled')