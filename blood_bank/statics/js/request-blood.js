// datepicker

window.onload = function () {

    document.getElementById('id_when_required').className += "flatpickr flatpickr-input";

    document.getElementsByClassName('form-group')[1].className += " d-flex";

    document.getElementsByClassName('sr-only')[2].className -= "sr-only";
    
    document.getElementsByTagName('LABEL')[1].className += " mr-3";

    document.getElementsByTagName('SELECT')[0].options[0].setAttribute("disabled","hidden");

    document.getElementsByTagName('SELECT')[1].options[0].setAttribute("disabled","hidden");

}

flatpickr("#id_when_required", {
    enableTime: true,
    dateFormat: "Y-m-d H:i",
});