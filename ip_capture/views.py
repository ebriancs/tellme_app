from django.views.generic import TemplateView
from django.views import View
from django.http import JsonResponse, HttpResponseRedirect
import json
import logging

from .models import UserDetail

logger = logging.getLogger('myapp')

class CaptureIPView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_ip'] = self.request.META.get('REMOTE_ADDR')
        context['csrf_token'] = self.request.META.get('CSRF_COOKIE')
        return context

class CaptureLocationView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            ip_address = request.META.get('REMOTE_ADDR')
            device_info = data.get('deviceInfo')

            UserDetail.objects.create(
                ip_address=ip_address,
                latitude=latitude,
                longitude=longitude,
                device_info=device_info
            )

            logger.debug(f"\nIP ADDRESS: {ip_address}\nLATITUDE: {latitude}\nLONGITUDE: {longitude}\nDEVICE INFO: {device_info}\n")

            return JsonResponse({'status': 'success'})
        except Exception as e:
            logger.error(f"Error capturing location: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
