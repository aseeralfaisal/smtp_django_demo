from django.urls import path
from .views import Views

urlpatterns = [
    path('', Views.SendMail),
]