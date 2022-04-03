from django.shortcuts import render
from django.views import View


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


class GalleryView(View):
    """ Представление галерея
    """
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'gallery.html', context)
