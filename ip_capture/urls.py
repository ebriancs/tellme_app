from django.urls import path
from .views import CaptureIPView, CaptureLocationView

urlpatterns = [
    path('', CaptureIPView.as_view(), name='capture_ip'),
    path('capture-location/', CaptureLocationView.as_view(), name='capture_location'),
]
