from django.shortcuts import render
from django.http import HttpResponse
from .models import Post , Content


def home(request):
    posts = Post.objects.all()

    return render(request, 'blog/home.html', {
        'posts': posts
    })

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'blog/post-detail.html', {
        'post': post
    })
def home1(request):
    posts = Content.objects.all()

    return render(request, 'blog/home.html', {
        'posts': posts
    })

def post_detail1(request, post_id):
    post = Content.objects.get(id=post_id)

    return render(request, 'blog/post-detail.html', {
        'post': post
    })