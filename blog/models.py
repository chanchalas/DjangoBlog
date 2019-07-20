from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title  = models.CharField(max_length=180)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_likes', null=True, blank=True)
    
    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'id':self.pk})    

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str('comments of '+str(self.post))

    class Meta:
        ordering = ['-created_at']