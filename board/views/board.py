from django.http import Http404, HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from konlpy.tag import Twitter
from konlpy.corpus import kolaw
from konlpy.utils import pprint
from nltk import collocations
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
        analyzed_data = twitter.pos(board.content, norm=True, stem=True)
        analyzed_data = [item[0] + "|" + item[1] for item in analyzed_data]
        response = BoardAnalyze.objects.create(
            board_id = board,
            result = ",".join(analyzed_data)
        )
        serializer = self.get_serializer(response)

        return Response(serializer.data)


class BoardCollocationsByBoardId(generics.RetrieveAPIView):

    serializer_class = BoardAnalyzeSerializer
    name = 'board-cotent-collocations'

    def retrieve(self, request, *args, **kwargs):

        jpype.attachThreadToJVM()
        board = Board.objects.get(pk=kwargs['pk'])
        measures = collocations.BigramAssocMeasures()
        tagged_words = Twitter().pos(board.content)
        finder = collocations.BigramCollocationFinder.from_words(tagged_words)
        result = finder.nbest(measures.pmi, 10) # top 5 n-grams with highest PMI
        text_result = ""
        for tuples in result:
            text_result += ",".join(tuples[0])
            text_result += "|"
            text_result += ",".join(tuples[1])

        response = BoardAnalyze.objects.create(
            board_id = board,
            result = text_result
        )
        serializer = self.get_serializer(response)
        return Response(serializer.data)
        
class BoardCollocationsExtractByBoardId(generics.RetrieveAPIView):

    serializer_class = BoardAnalyzeSerializer
    name = 'board-cotent-collocations-extract'

    def retrieve(self, request, *args, **kwargs):

        jpype.attachThreadToJVM()
        board = Board.objects.get(pk=kwargs['pk'])
        measures = collocations.BigramAssocMeasures()
        tagged_words = Twitter().pos(board.content)
        words = [w for w, t in tagged_words]
        ignored_words = [u'안녕']
        finder = collocations.BigramCollocationFinder.from_words(words)
        finder.apply_word_filter(lambda w: len(w) < 2 or w in ignored_words)
        finder.apply_freq_filter(3) # only bigrams that appear 3+ times
        result = finder.nbest(measures.pmi, 10)
        if result:
            text_result = ",".join(result[0])
        else:
            text_result = ""

        response = BoardAnalyze.objects.create(
            board_id = board,
            result = text_result
        )
        serializer = self.get_serializer(response)
        return Response(serializer.data)

