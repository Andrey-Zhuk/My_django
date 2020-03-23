from django.shortcuts import render

from .models import Post, Tag
# Create your views here.

def posts_list(reguest):
    posts = Post.objects.all()
    return render(reguest, "blog/index.html", context={"posts": posts})


def post_detail(reguest, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(reguest, "blog/post_detail.html", context={"post": post})


def tags_list(reguest):
    tags = Tag.objects.all()
    return render(reguest, "blog/tags_list.html", context={"tags": tags})


def tag_detail(reguest, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(reguest, "blog/tag_detail.html", context={"tag": tag})
