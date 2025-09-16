from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('register/<int:id>/', register_class, name='register_class'),
]
