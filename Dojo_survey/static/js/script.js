function required() {
    var empty = document.form.name.value;
    if (empty === "") {
        alert("You must put in a value");
        return false;
    }
    else {
        alert('Code has accepted : you can try another');
        return true;
    }
}


