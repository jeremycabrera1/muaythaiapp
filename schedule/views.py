from django.shortcuts import render, redirect

from .models import MuayClass1
from .forms import MuayClass1Form
# Create your views here.


def index(request):
    muay_class = MuayClass1.objects.all()

    if request.method == 'POST':
        form = MuayClass1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MuayClass1Form()

    context = {
        'muay_class': muay_class,
        'form': form
    }

    return render(request, 'schedule/index.html', context)
