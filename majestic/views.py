from django.shortcuts import render


def home(request):
    return render(request, 'majestic/base.html')


def price(request):
    return render(request, 'majestic/price.html')