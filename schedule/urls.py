from django.urls import path, include

from .views import index, about, register_class, thank_you, events, gallery, reviews, inquiry

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('gallery/', gallery, name='gallery'),
    path('reviews/', reviews, name='reviews'),
    path('inquiry/', inquiry, name='inquiry'),
    path('register/<int:id>/', register_class, name='register_class'),
    path('thank-you/', thank_you, name='thank_you'),
]

