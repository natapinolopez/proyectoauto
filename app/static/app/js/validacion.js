function validarFormulario() {


    var nombre = document.getElementById('nombre').value;
    var apellido = document.getElementById('apellido').value;
    var email = document.getElementById('email').value;
    var mensaje = document.getElementById('mensaje').value;


    if (nombre.trim() === '' || apellido.trim() === '' || email.trim() === '' || mensaje.trim() === '') {
        alert('Por favor, completa todos los campos.');
        return false;
    }


    var emailRegex = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;
    if (!email.match(emailRegex)) {
        alert('Por favor, ingresa un correo electrónico válido.');
        return false;
    }


    var contacto = {
        nombre: nombre,
        apellido: apellido,
        email: email,
        mensaje: mensaje
    };


    contactos.push(contacto);


    document.getElementById('nombre').value = '';
    document.getElementById('apellido').value = '';
    document.getElementById('email').value = '';
    document.getElementById('mensaje').value = '';

    alert('El formulario ha sido enviado con éxito.');


    return false;
}


var contactos = [];

