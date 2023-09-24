
function guardarPrimerValor () {
    var buttons = document.querySelectorAll("button");

    var valorBotonPresionado = "";

    buttons.forEach(function(button) {
        button.addEventListener("click", function() {
            valorBotonPresionado = button.value;
            localStorage.setItem('valorBotonPresionado', valorBotonPresionado);
            window.location.href = './pregunta_2.html';
            guardarSegundo();
        });
    });
}

function guardarSegundo () {
    const opciones = document.querySelector(".grid-container");
    var segundoPresionado = "";
    opciones.forEach(function(opcion) {
        opcion.addEventListener('click', function(){
            segundoPresionado = opcion.value;
            localStorage.setItem('valorBotonPresionado', localStorage.getItem('valorButtonPresionado') + segundoPresionado);
            window.location.href = "./pregunta_3";
        });
        
    })
}


function mostrar () {
    console.log("Redireccionado por el botón con valor: ", localStorage.getItem('valorBotonPresionado'));
}

function mostrar2() {
    console.log("Redireccionado por el botón con valor: ", localStorage.getItem('valorBotonPresionado'));
}

guardarPrimerValor();
