from django.db import models
from django.conf import settings

class News(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    main_image = models.ImageField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    counter = models.IntegerField(editable=False, default=0, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

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