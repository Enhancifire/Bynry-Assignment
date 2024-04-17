from django.db import models

from django.contrib.auth.models import User

REQUEST_TYPES = (
    ("NC", "New Connection"),
    ("BI", "Billing Issue"),
    ("LC", "Leakage Complaint"),
    ("OT", "Other"),
)

STATUS = (
    ("OP", "Open"),
    ("IP", "In Progress"),
    ("RE", "Resolved"),
)


class ServiceRequest(models.Model):
    request_id = models.UUIDField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    request_type = models.CharField(max_length=2, choices=REQUEST_TYPES)
    status = models.CharField(max_length=2, choices=STATUS)

    attachments = models.FileField(
        upload_to='attachments/',
        blank=True,
        null=True,
    )


class RequestNote(models.Model):
    service_request = models.ForeignKey(
        ServiceRequest,
        on_delete=models.CASCADE,
    )
    note = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
