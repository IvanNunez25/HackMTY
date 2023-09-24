
var buttons = document.querySelectorAll("button");

// Variable para almacenar el valor del botón presionado
var valorBotonPresionado = "";

// Agrega un event listener a cada botón
buttons.forEach(function(button) {
    button.addEventListener("click", function() {
        // Almacena el valor del botón presionado en la variable
        valorBotonPresionado = button.value;

        // Puedes realizar cualquier acción adicional que necesites aquí
        // Por ejemplo, puedes imprimir el valor en la consola
        console.log("Botón presionado: " + valorBotonPresionado);
        
        localStorage.setItem('valorBotonPresionado', valorBotonPresionado);
        window.location.href = './primera.html';


        window.location.href = './pregunta_2.html';
    });
});

function mostrar () {
    console.log("Redireccionado por el botón con valor: ", localStorage.getItem('valorBotonPresionado'));
}