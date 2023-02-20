from django.shortcuts import render
from .forms import FeedbackMessageForm


def home(request):
    return render(request, 'majestic/index.html')


def about(request):
    return render(request, 'majestic/about.html')


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


def qna(request):
    return render(request, 'majestic/qna.html')


def contacts(request):
    context = {
        'feedback': FeedbackMessageForm,
    }
    return render(request, 'majestic/contacts.html', context)

def privacy_policy(request):
    return render(request, 'majestic/privacy-policy.html')