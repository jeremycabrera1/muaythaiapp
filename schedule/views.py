from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from .models import MuayClass1
from .forms import MuayClass1Form, RegistrationForm
# Create your views here.


def index(request):
    muay_class = MuayClass1.objects.all().order_by('start_time')

    context = {
        'muay_class': muay_class,
    }

    return render(request, 'schedule/index.html', context)


def about(request):
    return render(request, 'schedule/about.html', {})


def thank_you(request):
    return render(request, 'schedule/thank_you.html', {})


def register_class(request, id):
    muay_class = get_object_or_404(MuayClass1, id=id)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = RegistrationForm()

    return render(request, 'schedule/registration_form.html', {
        'form': form,
        'muay_class': muay_class
    })
