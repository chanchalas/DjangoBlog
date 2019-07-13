from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import CreateBlogPostForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse


# Create your views here.

def home(request):
    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts':posts}
    return render(request, 'home.html', context)

def detail(request,id):
    post = get_object_or_404(BlogPost, pk=id)
    context = {'post':post}
    return render(request, 'detail.html',context)

def create_post(request):
    form = CreateBlogPostForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author=request.user
            instance.save()
            messages.success(request, message=f'{instance.title} post created successfully!!')
            return redirect('home')

    
    context = {'form':form}
    return render(request, 'create.html', context)


def edit_post(request, id):
        post = get_object_or_404(BlogPost, pk=id)
        form = CreateBlogPostForm(request.POST or None, instance=post)
        if request.POST:
            if form.is_valid():
                instance = form.save()
                messages.success(request, message=f'{instance.title} Post updated successfully!!')
                return redirect(reverse('detail',kwargs={'id':instance.pk}))
        
        context = {'form':form}
        return render(request, 'create.html', context)

def delete_post(request,id):
        post = get_object_or_404(BlogPost, pk=id)
        if request.POST:

            if post:
                post.delete()
                messages.warning(request,message='Post deleted successfully!!!')
                return redirect('home')   
        context = {'post':post}  
        return render(request,'delete.html',context)


def collapse(request):
        posts = BlogPost.objects.all()
        context = {'posts':posts}
        return render(request, 'collapse.html', context)

def modal(request):
        posts = BlogPost.objects.all()
        context = {'posts':posts}
        return render(request, 'modal.html', context)