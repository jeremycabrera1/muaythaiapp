from django.urls import path, include

from .views import index, about, register_class, thank_you

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('register/<int:id>/', register_class, name='register_class'),
    path('thank-you/', thank_you, name='thank_you'),  # callable function
]

