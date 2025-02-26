from django.urls import path, include
from .views import ListFood

urlpatterns = [
    path('v1/foods/', ListFood.as_view()),
]
