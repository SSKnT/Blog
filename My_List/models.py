from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Content =  models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("Detail_view", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.Title}"

    def get_absolute_url(self):
        return reverse("Detail_view", kwargs={"pk": self.post.pk})