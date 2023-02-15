from django.shortcuts import render


def home(request):
    return render(request, 'majestic/index.html')


def services(request):
    return render(request, 'majestic/services.html')

def vnkroe(request):
    return render(request, 'majestic/services/vnkroe.html')

def shevnash(request):
    return render(request, 'majestic/services/shevnash.html')

def vngotizd(request):
    return render(request, 'majestic/services/vngotizd.html')

def cerkvysh(request):
    return render(request, 'majestic/services/cerkvysh.html')


def price(request):
    return render(request, 'majestic/price.html')