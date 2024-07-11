from django.db import models
from django.utils import timezone

class UserDetail(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)
    device_info = models.JSONField(null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)