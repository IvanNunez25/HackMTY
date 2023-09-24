
function guardarPrimerValor () {
    var buttons = document.querySelectorAll("button");

    var valorBotonPresionado = "";

    buttons.forEach(function(button) {
        button.addEventListener("click", function() {
            valorBotonPresionado = button.value;
            localStorage.setItem('valorBotonPresionado', valorBotonPresionado);
            window.location.href = './index.html';
        });
    });
}




function mostrar () {
    console.log("Redireccionado por el botón con valor: ", localStorage.getItem('valorBotonPresionado'));
}

function mostrar2() {
    console.log("Redireccionado por el botón con valor: ", localStorage.getItem('valorBotonPresionado'));
}

guardarPrimerValor();
