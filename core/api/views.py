from rest_framework import generics
from core.models import Newsletter
from .serializers import NewsletterSerializer

class NewsletterListCreateAPIView(generics.ListCreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

