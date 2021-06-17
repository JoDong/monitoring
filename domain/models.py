from django.db import models
from core.models import HistoryModel


class UrlModel(HistoryModel):
    url_name = models.CharField(
        max_length=150,
        verbose_name='URL 이름')

    url = models.URLField(
        verbose_name='URL'
    )

    def __str__(self):
        return f'{self.url_name}'

    class Meta:
        db_table = 'url_model'
        verbose_name = 'Url'
        verbose_name_plural = 'Url'
