from django.urls import path
from .views import home,catag,login,contador,bodeguero,vendedor,admin

urlpatterns = [
     path('', home, name="archivo"),
     path('catalogo/', catag, name="catalogo"),
     path('account/',login, name="login"),
     path('contador/',contador,name="contador"),
     path('Bodeguero/',bodeguero, name="bodeguero"),
     path('vendedor/',vendedor,name="vendedor"),
     path('administrador/',admin,name="admin"),
]