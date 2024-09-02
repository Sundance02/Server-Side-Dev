from django.urls import path

from contact import views

urlpatterns = [
    path("contact/", views.contact_us, name="contact_us"),
    path("thanks/", views.thanks, name="thanks"),
]