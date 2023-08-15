from django.urls import path
from .views import find_restaurants

urlpatterns = [

    path('', find_restaurants, name="maps")
]