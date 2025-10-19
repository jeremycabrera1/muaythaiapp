from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from .forms import RegistrationForm, ReviewsForm
from .models import MuayClass1, Reviews
# Create your views here.


def index(request):
    muay_class = MuayClass1.objects.all().order_by('start_time')

    context = {
        'muay_class': muay_class,
    }

    return render(request, 'schedule/index.html', context)


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


def read_review(request):  # Should have named it read_review
    review = Reviews.objects.all().order_by('-date')
    
    context = {
        'review': review
    }
    return render(request, 'schedule/reviews.html', context)


def create_review(request):  # Should have named it create_review
    if request.method == 'POST':
        form = ReviewsForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('reviews')
    else:
        form = ReviewsForm()

    return render(request, 'schedule/create_review.html', {
        'form': form,
    })


def update_review(request, id):
    review = get_object_or_404(Reviews, pk=id)

    if request.method == 'POST':
        form = ReviewsForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews')  # back to review list
    else:
        form = ReviewsForm(instance=review)

    context = {
        'form': form,
        'edit': True
    }
    return render(request, 'schedule/create_review.html', context)


def delete_review(request, id):
    review = get_object_or_404(Reviews, pk=id)

    if request.method == 'POST':
        review.delete()
        return redirect('reviews')

    return render(request, 'schedule/delete_review_confirmation.html', {'review': review})


def inquiry(request):
    return render(request, 'schedule/inquiry.html', {})
