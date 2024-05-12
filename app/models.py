"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class SinglePost (models.Model):
    title = models.CharField(max_length = 128, verbose_name = "Заголовок")
    short_desc = models.CharField(blank = True, null = True, max_length = 512, verbose_name = "Краткое описание")
    text = models.TextField(verbose_name = "Основной текст")
    creation_date = models.DateField(default = datetime.now(), editable = False, verbose_name = "Дата создания", db_index = True)
    author = models.ForeignKey(User, null = True, blank = True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image_1 = models.ImageField(max_length = 255, null = True, blank = True, verbose_name = "Картинка (1)")
    image_2 = models.ImageField(max_length = 255, null = True, blank = True, verbose_name = "Картинка (2)")
    image_3 = models.ImageField(max_length = 255, null = True, blank = True, verbose_name = "Картинка (3)")

    def get_absolute_url(self):
        return reverse("singlepost", args=[str(self.id)])
    def __str__(self):
        return self.title

    class Meta:
        db_table = "single_posts"
        ordering = ["-creation_date", "title"]
        verbose_name = "одиночная публикация"
        verbose_name_plural = "одиночные публикации"

admin.site.register(SinglePost)

class Thread (models.Model):
    title = models.CharField(max_length = 192, verbose_name = "Название")
    short_desc = models.CharField(max_length = 512, verbose_name = "Краткое описание")
    theme = models.CharField(max_length = 32, db_default = "00", default = "Неспецифический заговор",
                             verbose_name = "Тематика", choices = [
                                ("AL", "Инопланетная жизнь"),
                                ("CU", "Таинственные культы"),
                                ("GV", "Правительственный заговор"),
                                ("IL", "Заговор иллюминатов"),
                                ("RI", "Мировая элита"),
                                ("00", "Неспецифический заговор"),
                            ])
    owner = models.ForeignKey(User, null = True, blank = True, on_delete=models.SET_NULL, verbose_name = "Владелец")
    created = models.DateTimeField(default = datetime.now(), verbose_name = "Создание")
    active = models.DateTimeField(default = datetime.now(), verbose_name = "Последняя активность")
    image = models.ImageField(max_length = 255, null = True, blank = True, verbose_name = "Картинка")

    def get_absolute_url(self):
        return reverse("thread", args=[str(self.id)])
    def __str__(self):
        return self.title

    class Meta:
        db_table = "threads"
        ordering = ["-active", "-created"]
        verbose_name = "форумная публикация"
        verbose_name_plural = "форумные публикации"

admin.site.register(Thread)

class ThreadComment (models.Model):
    homethread = models.ForeignKey(Thread, on_delete = models.CASCADE, verbose_name = "Форум")
    author = models.ForeignKey(User, null = True, blank = True, on_delete=models.SET_NULL, verbose_name = "Автор")
    text = models.TextField(verbose_name = "Текст")
    created = models.DateTimeField(default = datetime.now(), verbose_name = "Создание")
    image_1 = models.ImageField(max_length = 255, null = True, blank = True, verbose_name = "Картинка (1)")
    image_2 = models.ImageField(max_length = 255, null = True, blank = True, verbose_name = "Картинка (2)")
    image_3 = models.ImageField(max_length = 255, null = True, blank = True, verbose_name = "Картинка (3)")

    def __str__(self):
        return str(self.homethread)+" | "+str(self.author)+" | "+self.text[:16]

    class Meta:
        db_table = "thread_comments"
        ordering = ["created"]
        verbose_name = "комментарий форума"
        verbose_name_plural = "комментарии форума"

admin.site.register(ThreadComment)