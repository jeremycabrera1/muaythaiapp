from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            signup = form.save(commit=False)
            signup.save()

    else:
        form = UserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'registration/signup.html', context)