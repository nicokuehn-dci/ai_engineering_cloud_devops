from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post
from django.views.generic.detail import DetailView


class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = "post"

















# test will still work if you use a function
def lst_view(request):
    return render(request, "posts/list.html", {"posts": Post.objects.all()})
