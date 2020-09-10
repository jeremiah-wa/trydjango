from django.db import models


# Create your models here.
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    content = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("articles:article-list", kwargs={"id": self.id})