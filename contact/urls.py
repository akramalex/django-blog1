from django.urls import path
from .views import collaborate_view, collaborate_success

urlpatterns = [
    path('collaborate/', collaborate_view, name='collaborate'),  # URL for the contact form
    path('collaborate/success/', collaborate_success, name='collaborate_success'),  # URL for the success page
]