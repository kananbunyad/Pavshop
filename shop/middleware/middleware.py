from django.utils import timezone
from django.http import HttpResponseForbidden
from account.models import Blacklist 

class IPBlacklistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = request.META.get('REMOTE_ADDR')
        now = timezone.now()
        blacklist_entries = Blacklist.objects.filter(
            ip_address=client_ip,
            is_active=True
        )

        for entry in blacklist_entries:
            end_time = entry.start_time + entry.duration
            if entry.start_time <= now <= end_time:
                return HttpResponseForbidden('Access denied: Your IP address has been temporarily blacklisted.')

        response = self.get_response(request)
        return response
