from django.urls import path
from . import views


app_name = 'majestic'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/vyshivka-na-kroe', views.vnkroe, name='vnkroe'),
    path('services/shevrony-i-nashivki', views.shevnash, name='shevnash'),
    path('services/vyshivka-na-gotovyh-izdeliyah', views.vngotizd, name='vngotizd'),
    path('services/cerkovnaya-vyshivka', views.cerkvysh, name='cerkvysh'),
    path('price/', views.price, name='price'),
    path('contacts/', views.contacts, name='contacts'),
    path('qna/', views.qna, name='qna'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
]
