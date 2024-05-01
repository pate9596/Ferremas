const Api_url = 'https://mindicador.cl';

const xhr = new XMLHttpRequest();

function onRequestHandler(){
    if(this.readyState === 4 && this.status === 200){
        const data = JSON.parse(this.response);
        
        const dolarValor = data.dolar.valor; 
        const items = document.querySelectorAll("#u");//No se me ocurrio nada creativo fdsfgsjdfdfsg

        items.forEach(item => {
            const precioItem = item.querySelector("#i");
            const precioActual = parseFloat(precioItem.innerText.replace('$', '').replace(',', ''));
            const nuevoPrecio = (precioActual * dolarValor).toFixed(0); // Redondear a 0 decimales xd
            precioItem.innerText = `$${nuevoPrecio}`;
        });
    }
}

xhr.addEventListener("load",onRequestHandler);//Aqui hice unas cosas pero no hacen ninguna cuestion xd
xhr.open("GET", `${Api_url}/api`);
xhr.send();
