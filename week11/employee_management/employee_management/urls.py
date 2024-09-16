from django.contrib import admin
from django.urls import path, include
from employee import views

urlpatterns = [
    path("employee/", include("employee.urls")),
]
