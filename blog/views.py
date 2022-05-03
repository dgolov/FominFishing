from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Category, Post


class BlogView(ListView):
    """ Представление видео галереи
    """
    template_name = 'blog.html'
    context_object_name = "blog"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['title'] = 'Блог'
        return context

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object.title
        return context
