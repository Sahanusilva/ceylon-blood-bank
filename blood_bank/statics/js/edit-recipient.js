window.onload = function () {
    var element = document.getElementById("id_completed_date");
    element.classList.add("flatpickr flatpickr-input");
}

flatpickr("#id_completed_date", {
    enableTime: true,
    dateFormat: "Y-m-d H:i",    
});