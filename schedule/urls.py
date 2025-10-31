from django.urls import path, include

from .views import index, about, register_class, thank_you, events, gallery, read_review, inquiry, create_review, thank_you_review, update_review, delete_review, my_classes

urlpatterns = [
    path('', index, name='home'),
    path('my-classes/', my_classes, name='my_classes'),
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('gallery/', gallery, name='gallery'),
    path('reviews/', read_review, name='reviews'),
    path('leave-a-review/', create_review, name='create_review'),
    path('update-review/<int:id>/', update_review, name='update_review'),
    path('delete-review/<int:id>/', delete_review, name='delete_review'),
    path('inquiry/', inquiry, name='inquiry'),
    path('register/<int:id>/', register_class, name='register_class'),
    path('thank-you/', thank_you, name='thank_you'),
    path('thank-you-review/', thank_you_review, name='thank_you_review'),
]

