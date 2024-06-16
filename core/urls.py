from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'Producto', views.ProductoView)
urlpatterns = [
     path('', views.home, name="archivo"),
     path('catalogo/', views.catag, name="catalogo"),
    
     path('contador/',views.contador,name="contador"),
     path('Bodeguero/',views.bodeguero, name="bodeguero"),
     path('Bodeproducs/', views.bodegp, name="bodeproducs"),
     path('vendedor/',views.vendedor,name="vendedor"),
     path('administrador/',views.admin,name="admin"),
     path('sesion', views.regis,name="regis"),
     path('api/',include(router.urls)),
     path('iniciar_pago/', views.iniciar_pago, name='iniciar_pago'),
     path('pago_confirmado/', views.pago_confirmado, name='pago_confirmado'),
]#Xd