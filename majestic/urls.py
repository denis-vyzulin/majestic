from django.urls import path
from . import views


app_name = 'majestic'
urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('services/vyshivka-na-kroe', views.vnkroe, name='vnkroe'),
    path('services/shevroni-i-nashivki', views.shevnash, name='shevnash'),
    path('services/vyshivka-na-gotovyh-izdeliyah', views.vngotizd, name='vngotizd'),
    path('services/cerkovnaya-vishivka', views.cerkvysh, name='cerkvysh'),
    path('price/', views.price, name='price'),
]
