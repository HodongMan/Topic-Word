from django.urls import path

from .views import BoardList, BoardDetail, BoardAnalizeByBoardId


urlpatterns = [
    path("board/", BoardList.as_view(), name=BoardList.name),
    path("board/<int:pk>/", BoardDetail.as_view(), name=BoardDetail.name),
    path("board/analyze/<int:pk>/", BoardAnalizeByBoardId.as_view(), name=BoardAnalizeByBoardId.name),
]