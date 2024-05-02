from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name="archivo"),
     path('catalogo/', views.catag, name="catalogo"),
     path('account/',views.login, name="login"),
     path('contador/',views.contador,name="contador"),
     path('Bodeguero/',views.bodeguero, name="bodeguero"),
     path('vendedor/',views.vendedor,name="vendedor"),
     path('administrador/',views.admin,name="admin"),
]