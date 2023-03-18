from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class User(models.Model):
    email = models.TextField()
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)


class Post(models.Model):
    title = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = ArrayField(models.CharField(max_length=100), null=True)

    class Meta:
        indexes = [
            models.Index(fields=["title"]),
        ]
