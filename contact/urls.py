from django.urls import path
from .views import collaborate_view, collaborate_success

urlpatterns = [
    path('collaborate/', collaborate_view, name='collaborate'),  # Ensure this name matches your test
    path('collaborate/success/', collaborate_success, name='collaborate_success'),
]