from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Producto
from .serializer import Apiproducto
from django.urls import reverse
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
from transbank.common.integration_type import IntegrationType
from django.conf import settings


# Create your views here.
def home(request): 
    return render(request, "consola/index.html")

def catag(request): 
    return render(request, "consola/catalogo.html")


def contador(request): 
    return render(request, "consola/Contador/cont.html")

def bodeguero(request): 
    return render(request, "consola/Bodeguero/Bode.html")
def bodegp(request): 
    return render(request, "consola/Vendedor/BodePr.html")


def vendedor(request): 
    return render(request, "consola/Vendedor/vende.html")

def admin(request): 
    return render(request, "consola/Administrador/Adm.html")

def regis(request):
    return render(request, "consola/Registrase/Registrar.html")




#api
class ProductoView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = Apiproducto


def iniciar_pago(request):
    transaction = Transaction(WebpayOptions(
        commerce_code='597055555532',             # Test commerce code
        api_key='579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C',                 
        integration_type=IntegrationType.TEST     # Use TEST for sandbox
    ))
    response = transaction.create(
        buy_order='order123456789',
        session_id='session123456',
        amount=100000,                              # Amount in CLP
        return_url=request.build_absolute_uri(reverse('pago_confirmado'))
    )
    return redirect(response['url'] + '?token_ws=' + response['token'])

def pago_confirmado(request):
    token = request.GET.get('token_ws')
    transaction = Transaction(WebpayOptions(
        commerce_code='597055555532',             # Test commerce code
        api_key='579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C',                
        integration_type=IntegrationType.TEST     # Use TEST for sandbox
    ))
    response = transaction.commit(token)
    
    if response['status'] == 'AUTHORIZED':
        return render(request, 'consola/pago_aprobado.html', {'response': response})
    else:
        return render(request, 'consola/pago_fallado.html', {'response': response})