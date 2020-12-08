window.onload = function () {
    var element = document.getElementById("id_datetime");
    element.classList.add("flatpickr flatpickr-input");
}

flatpickr("#id_datetime", {
    enableTime: true,
    dateFormat: "Y-m-d H:i",    
});