from django.http import Http404, HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from konlpy.tag import Twitter
import jpype

from ..models import Board, BoardAnalyze
from ..serializers import BoardSerializer, BoardAnalyzeSerializer

twitter = Twitter()
jpype.attachThreadToJVM()

class BoardList(generics.ListCreateAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'board-list'

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'board-detail'

class BoardAnalizeByBoardId(generics.RetrieveAPIView):

    serializer_class = BoardAnalyzeSerializer
    name = 'board-cotent-analyze'

    def retrieve(self, request, *args, **kwargs):

        jpype.attachThreadToJVM()
        board = Board.objects.get(pk=kwargs['pk'])
        analyzed_data = twitter.pos(board.content)
        analyzed_data = [item[0] + "|" + item[1] for item in analyzed_data]
        response = BoardAnalyze.objects.create(
            board_id = board,
            result = ",".join(analyzed_data)
        )
        serializer = self.get_serializer(response)

        return Response(serializer.data)
        

