function login() {
    var usuario = document.getElementById('username').value;
    var contrasena = document.getElementById('password').value;

    // Extraer la parte después del "@" del nombre de usuario
    var domain = usuario.split('@')[1];

    switch (domain) {
        case 'admin.com':
            if (contrasena === 'admin') {
                window.location.href = 'Administrador/Adm.html';
            } else {
                alert('Contraseña incorrecta para administrador.');
            }
            break;
        case 'vendedor.com':
            if (contrasena === 'vendedor') {
                window.location.href = 'Vendedor/vende.html';
            } else {
                alert('Contraseña incorrecta para vendedor.');
            }
            break;
        case 'cliente.com':
            if (contrasena === 'cliente') {
                window.location.href = 'cliente_dashboard.html';
            } else {
                alert('Contraseña incorrecta para cliente.');
            }break;
        case 'contador.com' :
            if(contrasena == 'contador'){
                window.location.href = 'Contador/cont.html'
            } else {
                alert('Contraseña incorrecta para contador.');
            }break;
        case 'bodeguero.com':
            if(contrasena == 'bodeguero'){
                window.location.href = 'Bodeguero/bode.html'
            }else{
                alert("Contraseña Incorrecta para Bodeguero")
            }break;
        default:
            alert('Dominio de correo electrónico no válido.');
            break;
    }
}
