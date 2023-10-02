from django.db import models
from django.conf import settings

class News(models.Model):
    title = models.CharField(max_length=250, verbose_name="Тема")
    description = models.TextField(verbose_name="Описание")
    main_image = models.ImageField(verbose_name="Главное изоб")
    text = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    counter = models.IntegerField(editable=False, default=0, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    like_count = models.IntegerField(editable=False, default=0, blank=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class NewsImages(models.Model):
    newsObject = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField()

class Gallery(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField()

class NewsDetails(models.Model):
    newsObject = models.ForeignKey(News, on_delete=models.CASCADE)
    title = models.CharField(max_length=240)
    text = models.TextField()
    def __str__(self):
        return f"{self.newsObject.title} - {self.title}"

class Comments(models.Model):
    newsObject = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
