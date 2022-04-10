from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Photo


class MainView(View):
    """ Представление главной страницы
    """
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'index.html', context)


class AboutView(View):
    """ Представление страницы обо мне
    """
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'about.html', context)


class BoatView(View):
    """ Представление страницы о лодке
    """
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'boat.html', context)


class ContactView(View):
    """ Представление страницы контакты
    """
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'contact.html', context)


class ServiceView(View):
    """ Представление страницы услуги
    """
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'service.html', context)


class GalleryView(ListView):
    """ Представление галерея
    """
    template_name = 'gallery.html'
    context_object_name = "photos"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context['title'] = 'Галерея трофеев'
        return context

    def get_queryset(self):
        return Photo.objects.all()
