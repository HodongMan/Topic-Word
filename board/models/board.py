from django.db import models

class Board(models.Model):

    user = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    background_color = models.CharField(max_length=200, default="")
    color = models.CharField(max_length=200, default="")
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

class BoardAnalyze(models.Model):

    board_id = models.ForeignKey(
        Board,
        related_name='board',
        on_delete=models.CASCADE
    )
    result = models.TextField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-board_id', )