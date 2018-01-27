from django.db import models

from .board import Board

class Keyword(models.Model):

    board_id = models.ForeignKey(
        Board,
        related_name='board_keyword',
        on_delete=models.CASCADE,
    )
    keyword = models.CharField(max_length=500)
    sentence = models.TextField()

    class Meta:
        ordering = ('-board_id',)