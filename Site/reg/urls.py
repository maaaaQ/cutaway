from django.urls import path
from .views import views

urlpatterns = [
    path("registration/", views.registration, name="registration"),
]
