from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Photo, Video, Service, Calendar
from .mixins import FormMixin


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


class ServiceView(ListView, FormMixin):
    """ Представление страницы услуги
    """
    template_name = 'service.html'
    context_object_name = "services"
    success_form_url = 'service'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServiceView, self).get_context_data(**kwargs)
        context['title'] = 'Услуги рыболовного гида'
        context['form'] = self.form
        return context

    def get_queryset(self):
        return Service.objects.filter(is_active=True)


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


class VideoView(ListView, FormMixin):
    """ Представление видео галереи
    """
    template_name = 'video.html'
    context_object_name = "videos"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VideoView, self).get_context_data(**kwargs)
        context['title'] = 'Видео'
        return context

    def get_queryset(self):
        return Video.objects.filter(in_active=True)


class AdvertisingView(View):
    """ Представление страницы рекламы
    """
    def get(self, request, *args, **kwargs):
        context = {
            "title": "Реклама"
        }
        return render(request, 'advertising.html', context)


class CalendarView(ListView, FormMixin):
    """ Представление видео галереи
    """
    template_name = 'calendar.html'
    context_object_name = "calendar"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CalendarView, self).get_context_data(**kwargs)
        context['title'] = 'Календарь рыбалок'
        context['form'] = self.form
        return context

    def get_queryset(self):
        return Calendar.objects.all()
