from django.urls import path

from .views import BoardList, BoardDetail


urlpatterns = [
    path("board/", BoardList.as_view(), name=BoardList.name),
    path("board/<int:pk>/", BoardDetail.as_view(), name=BoardDetail.name),
]