from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import Post, Tag

from .utils import ObjectDetailMixin
from .forms import TagForm


# Create your views here.
def posts_list(reguest):
    posts = Post.objects.all()
    return render(reguest, "blog/index.html", context={"posts": posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = "blog/post_detail.html"
    # def get(self, reguest, slug):
    #     post = get_object_or_404(Post, slug__iexact=slug)
    #     return render(reguest, "blog/post_detail.html", context={"post": post})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = "blog/tag_detail.html"
    # def get(self, reguest, slug):
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(reguest, "blog/tag_detail.html", context={"tag": tag})

class TagCreate(View):
    def get(self, reguest):
        form = TagForm()
        return render(reguest, "blog/tag_create.html", context={"form": form})

    def post(self, reguest):
        bound_form = TagForm(reguest.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(reguest, "blog/tag_create.html", context={"form": bound_form})



def tags_list(reguest):
    tags = Tag.objects.all()
    return render(reguest, "blog/tags_list.html", context={"tags": tags})




