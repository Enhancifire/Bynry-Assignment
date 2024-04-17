from django.contrib import admin
from .models import ServiceRequest, RequestNote

admin.site.register(ServiceRequest)
admin.site.register(RequestNote)
