from django.urls import path
from .views import create_request, view_request, view_all_requests

urlpatterns = [
    path("new/", create_request, name="create_request"),
    path("<str:id>/", view_request, name="view_request"),
    path("", view_all_requests, name="view_all_request"),
]
