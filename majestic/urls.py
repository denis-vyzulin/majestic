from django.urls import path
from . import views


app_name = 'majestic'
urlpatterns = [
    path('', views.home, name='home'),
    path('price/', views.price, name='price'),
]