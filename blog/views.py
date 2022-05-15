from django.views.generic import ListView, DetailView

from .models import Post
from web.mixins import FormMixin


class BlogView(ListView):
    """ Представление блога
    """
    template_name = 'blog.html'
    context_object_name = "blog"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['title'] = 'Блог'
        return context

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView, FormMixin):
    """ Представление поста блога
    """
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object.title
        context['form'] = self.form
        return context
