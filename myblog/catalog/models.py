from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'


class PostComment(models.Model):
    user_name = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return f'Отзыв от {self.user_name} ({self.email})'