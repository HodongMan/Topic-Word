from rest_framework import generics

from ..models import Crime
from ..serializers import CrimeSerializer


class CrimeList(generics.ListCreateAPIView):

    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer
    name = 'crime-list'

class CrimeDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer
    name = 'crime-detail'