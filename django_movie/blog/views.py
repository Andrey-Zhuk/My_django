from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import Post, Tag
# Create your views here.

def posts_list(reguest):
    posts = Post.objects.all()
    return render(reguest, "blog/index.html", context={"posts": posts})


class PostDetail(View):
    def get(self, reguest, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(reguest, "blog/post_detail.html", context={"post": post})


class TagDetail(View):
    def get(self, reguest, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(reguest, "blog/tag_detail.html", context={"tag": tag})


def tags_list(reguest):
    tags = Tag.objects.all()
    return render(reguest, "blog/tags_list.html", context={"tags": tags})




