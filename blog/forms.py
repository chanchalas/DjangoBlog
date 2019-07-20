from django import forms
from .models import BlogPost, Comment

class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model  = BlogPost
        fields = ['title','content'] 


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']