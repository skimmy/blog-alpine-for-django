from django.urls import path

from . import views

urlpatterns = [
    path("", views.alpine_view, name="index")
]
