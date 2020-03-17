from django.shortcuts import render

from .models import Post
# Create your views here.

def posts_list(reguest):
    posts = Post.objects.all()
    return render(reguest, "blog/index.html", context={"posts": posts})


def post_detail(reguest, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(reguest, "blog/post_detail.html", context={"post": post})