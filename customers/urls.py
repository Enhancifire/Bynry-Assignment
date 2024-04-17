from django.urls import path
from .views import create_profile, check_profile, get_profile

urlpatterns = [
    path("new/", create_profile, name="create_profile"),
    path("check/", check_profile, name="check_profile"),
]
