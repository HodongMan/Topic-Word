from rest_framework import serializers

from ..models import Board

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
