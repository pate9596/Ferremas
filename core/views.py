from django.shortcuts import render

# Create your views here.
def home(request): 
    return render(request, "consola/index.html")

def catag(request): 
    return render(request, "consola/catalogo.html")

def login(request): 
    return render(request, "consola/account.html")

def contador(request): 
    return render(request, "consola/Contador/cont.html")

def bodeguero(request): 
    return render(request, "consola/Bodeguero/Bode.html")

def vendedor(request): 
    return render(request, "consola/Vendedor/vende.html")

def admin(request): 
    return render(request, "consola/Administrador/Adm.html")