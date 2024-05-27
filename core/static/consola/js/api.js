const Api_url = 'https://mindicador.cl';

const xhr = new XMLHttpRequest();


function onRequestHandler(){
    if(this.readyState === 4 && this.status === 200){
        const data = JSON.parse(this.response);
        
        const dolarValor = data.dolar.valor; //se llama la la variable dolar y uf  de la api
        const ufValor = data.uf.valor;


        const items = document.querySelectorAll("#u");//No se me ocurrio nada creativo fdsfgsjdfdfsg (es el nombre de la id)

        items.forEach(item => {
            const precioItem = item.querySelector("#i"); //(ese igual )

            const precioActual = parseFloat(precioItem.innerText.replace('$', '').replace(',', ''));


            const nuevoPrecio = (precioActual / dolarValor).toFixed(2); // Redondear a 0 decimales xd
 
            precioItem.innerText = `$${nuevoPrecio}`;

        });

        const itemsUF = document.querySelectorAll("#u .precio-item-uf");

        itemsUF.forEach(item => {
            const precioActual = parseFloat(item.innerText.replace('$', '').replace(',', ''));
            const nuevoPrecioUF = (precioActual / ufValor).toFixed(2); 
            item.innerText = `$${nuevoPrecioUF}`;
        });
    }
}


xhr.addEventListener("load",onRequestHandler);//Aqui hice unas cosas pero no hacen ninguna cuestion xd
xhr.open("GET", `${Api_url}/api`);
xhr.send();









/*

function cambiarMoneda() {
    const precios = document.querySelectorAll('.precio-item');
    const dolarValor = data.dolar.valor;

    precios.forEach(precio => {
        const precioActual = parseFloat(precio.innerText.replace('$', '').replace(',', ''));
        const nuevoValor = (precioActual / dolarValor).toFixed(2);
        precio.innerText = `$${nuevoValor} USD`;
    });

    const botonMoneda = document.getElementById('cambiarMoneda');
    botonMoneda.textContent = 'Cambiar a CLP';
    botonMoneda.setAttribute('onclick', 'cambiarMonedaCLP()');
}

function cambiarMonedaCLP() {
    const precios = document.querySelectorAll('.precio-item');
    const dolarValor = data.dolar.valor;

    precios.forEach(precio => {
        const precioActual = parseFloat(precio.innerText.replace('$', '').replace(',', ''));
        const nuevoValor = precioActual * dolarValor;
        precio.innerText = `$${nuevoValor.toFixed(2)} CLP`;
    });

    const botonMoneda = document.getElementById('cambiarMoneda');
    botonMoneda.textContent = 'Cambiar a USD';
    botonMoneda.setAttribute('onclick', 'cambiarMoneda()');
}
*/