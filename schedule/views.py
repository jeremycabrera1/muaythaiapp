from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from .models import MuayClass1, Reviews
from .forms import MuayClass1Form, RegistrationForm, ReviewsForm
# Create your views here.


def index(request):
    muay_class = MuayClass1.objects.all().order_by('start_time')

    context = {
        'muay_class': muay_class,
    }

    return render(request, 'schedule/index.html', context)


def about(request):
    return render(request, 'schedule/about.html', {})


def events(request):
    return render(request, 'schedule/events.html', {})


def gallery(request):
    return render(request, 'schedule/gallery.html', {})


def thank_you(request):
    return render(request, 'schedule/thank_you.html', {})


def thank_you_review(request):
    return render(request, 'schedule/thank_you_review.html')


def reviews(request):
    reviews = Reviews.objects.all().order_by('-date')
    context = {
        'reviews': reviews
    }
    return render(request, 'schedule/reviews.html', context)


def leave_a_review(request):
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('thank_you_review')
    else:
        form = ReviewsForm()

    return render(request, 'schedule/leave_a_review.html', {
        'form': form,
    })


def inquiry(request):
    return render(request, 'schedule/inquiry.html', {})


def register_class(request, id):
    muay_class = get_object_or_404(MuayClass1, id=id)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
        'muay_class': muay_class
    }

    return render(request, 'schedule/registration_form.html', context)
