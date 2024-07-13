from django.urls import path
from .views import APi

urlpatterns = [
    path('', APi, name="APi")
]