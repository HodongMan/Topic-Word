from rest_framework import serializers

from ..models import Board, BoardAnalyze

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = (
            'pk',
            'user',
            'title',
            'content',
            'background_color',
            'color',
            'created',
            'updated'
        )

class BoardAnalyzeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoardAnalyze
        fields = (
            'pk',
            'board_id',
            'result',
            'created',
        )