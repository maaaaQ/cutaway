from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class News(models.Model):
    title = models.CharField("Название статьи", max_length=150)
    text = models.TextField("Текст статьи")
    date = models.DateTimeField("Дата и время", auto_now=False, auto_now_add=False)
    autor = models.ForeignKey(User, verbose_name=("Автор"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
