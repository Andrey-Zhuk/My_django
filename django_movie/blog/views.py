from django.shortcuts import render

# Create your views here.

def posts_list(reguest):
    n = ["oleg","masha", "vala"]
    return render(reguest, "blog/index.html", context={"name": n})