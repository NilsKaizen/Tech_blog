from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    draft = models.BooleanField(default=True)
    date_c = models.DateTimeField(auto_now_add=True)
    date_p = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=DO_NOTHING)

    def __str__(self):
        return self.title + ' Author: ' + self.author.name

    def publish(self):
        self.draft = False
        self.date_p = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved=True)


class Comment(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    approved = models.BooleanField(default=False)
    date_c = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=DO_NOTHING)

    def approve(self):
        
        self.approved = True
        self.save()

    def __str__(self):
        return self.text
