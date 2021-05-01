from django.db import models


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(verbose_name='Дата')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.CharField(max_length=1000, verbose_name='Текст')

    def __str__(self):
        return self.title


class Tokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=100, verbose_name='Ключ')

    def __str__(self):
        return self.token