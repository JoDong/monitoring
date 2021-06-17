from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Your Login ID',
        verbose_name='아이디'
    )

    first_name = models.CharField(
        max_length=30,
        verbose_name='이름',
    )

    email = models.EmailField(
        max_length=60,
        blank=True,
        help_text='사용자 이메일입니다.',
        verbose_name='이메일',
    )

    phone = models.CharField(
        max_length=25,
        blank=False,
        unique=True,
        help_text='사용자 번호입니다.',
        verbose_name='핸드폰 번호',
    )

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        db_table = 'user-table'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
