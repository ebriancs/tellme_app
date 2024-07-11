from django.db import models
from django.utils import timezone

class UserDetail(models.Model):
    ip_address = models.GenericIPAddressField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    device_info = models.JSONField()
