from django.db import models
from core.models import HistoryModel
from domain.models import UrlModel


class StatusLog(HistoryModel):
    url = models.ForeignKey(UrlModel, on_delete=models.CASCADE, verbose_name='Url')
    status = models.CharField(max_length=10, verbose_name='상태코드')
    process = models.CharField(max_length=100, verbose_name='처리시간')

    class Meta:
        db_table = 'url_status'
        verbose_name = '상태로그'
        verbose_name_plural = '상태로그'
