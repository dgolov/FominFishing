from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from .models import Photo
from .mixins import FormMixin
from .forms import RequestForm


class MainView(View, FormMixin):
    """ Представление главной страницы
    """
    def get(self, request, *args, **kwargs):
        photo = Photo.objects.all().filter(in_main_page=True)
        context = {
            "photos": photo,
            "title": "Рыбалка с гидом в Нижегородской области",
            'form': self.form,
        }
        return render(request, 'index.html', context)


class AboutView(View, FormMixin):
    """ Представление страницы обо мне
    """
    success_form_url = 'about'

    def get(self, request, *args, **kwargs):
        context = {
            "title": "Трофейная рыбалка с Андреем Фоминым",
            'form': self.form
        }
        return render(request, 'about.html', context)


class BoatView(View):
    """ Представление страницы о лодке
    """
    def get(self, request, *args, **kwargs):
        context = {
            "title": "Моя лодка"
        }
        return render(request, 'boat.html', context)


class ContactView(View, FormMixin):
    """ Представление страницы контакты
    """
    success_form_url = 'contact'

    def get(self, request, *args, **kwargs):
        context = {
            "title": "Контакты",
            'form': self.form
        }
        return render(request, 'contact.html', context)


class ServiceView(View, FormMixin):
    """ Представление страницы услуги
    """
    success_form_url = 'service'

    def get(self, request, *args, **kwargs):
        context = {"title": "Услуги рыболовного гида", 'form': self.form}
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
