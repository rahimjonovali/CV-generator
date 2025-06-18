from rest_framework import generics
from .models import CV
from .serializers import CVSerializer

class CVListCreateAPIView(generics.ListCreateAPIView):
     queryset = CV.objects.all()
     serializer_class = CVSerializer

class CVDetailAPIView(generics.RetrieveAPIView):
     queryset = CV.objects.all()
     serializer_class = CVSerializer
