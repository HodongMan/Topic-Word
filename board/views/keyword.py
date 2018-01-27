from rest_framework import generics

from ..models import Keyword
from ..serializers import KeywordSerializer

class KeywordList(generics.ListCreateAPIView):

    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    name = 'keyword-list'

class KeywordDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    name = 'keyword-detail'