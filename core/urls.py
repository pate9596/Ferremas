from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'Producto', views.ProductoView)
urlpatterns = [
     path('', views.home, name="archivo"),
     path('catalogo/', views.catag, name="catalogo"),
     path('account/',views.login, name="login"),
     path('contador/',views.contador,name="contador"),
     path('Bodeguero/',views.bodeguero, name="bodeguero"),
     path('vendedor/',views.vendedor,name="vendedor"),
     path('administrador/',views.admin,name="admin"),
     path('api/',include(router.urls)),
     path('initiate_payment/', views.initiate_payment, name='initiate_payment'),
     path('payment_confirm/', views.payment_confirm, name='payment_confirm'),
]#Xd