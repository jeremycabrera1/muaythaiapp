from django.shortcuts import render, redirect, HttpResponse

from .models import MuayClass1
from .forms import MuayClass1Form
# Create your views here.


def index(request):
    muay_class = MuayClass1.objects.all().order_by('start_time')

    context = {
        'muay_class': muay_class,
    }

    return render(request, 'schedule/index.html', context)

def about(request):
    return render(request, 'schedule/about.html', {})


def register_class(request, id):
    return HttpResponse(f"Registering for class {id}")