from django.urls import path

from .views import CrimeList, CrimeDetail

urlpatterns = [
    path('crime/', CrimeList.as_view(), name=CrimeList.name),
    path('crime/<int:pk>/', CrimeDetail.as_view(), name=CrimeDetail.name),
]