from django.shortcuts import render, redirect

from .forms import CustomCreationForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            signup = form.save(commit=False)
            signup.save()
            return redirect('home')

    else:
        form = CustomCreationForm()

    context = {
        'form': form
    }

    return render(request, 'registration/signup.html', context)