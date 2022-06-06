import logging

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from .forms import ReviewForm
from .models import Photo, Video, Service, Calendar, Review
from .mixins import FormMixin


logger = logging.getLogger(__name__)


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


class BoatView(View, FormMixin):
    """ Представление страницы о лодке
    """
    def get(self, request, *args, **kwargs):
        context = {
            "title": "Моя лодка",
            'form': self.form
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


class ReviewView(ListView):
    """ Представление страницы отзывов
    """
    template_name = 'reviews.html'
    context_object_name = "reviews"
    success_form_url = ''
    form = ReviewForm()

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        logger.debug('[ReviewView] - Try to post review')
        if form.is_valid():
            form.save()
            logger.info('[ReviewView] Post review successfully')
            messages.add_message(request, messages.SUCCESS, 'Благодарю Вас за отзыв!')
            try:
                logger.debug('[ReviewView] - Try to send mail')
                send_mail(
                    'Опубликован отзыв на сайте',
                    'Опубликован отзыв на сайте av-fomin.ru, необходимо подтвердить подерацию.',
                    'myvmeste_info@mail.ru',
                    ['dgolov@icloud.com'],
                    fail_silently=False
                )
            except Exception as e:
                logger.error(f'[ReviewView] Send mail failed: {e}')
            return HttpResponseRedirect(f'/{self.success_form_url}#review')
        logger.error('[ReviewView] Post review failed')
        messages.add_message(request, messages.ERROR, 'Произошла ошибка! Попробуйте повторить запрос позже.')
        return HttpResponseRedirect('/reviews')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        context['title'] = 'Отзывы'
        context['form'] = self.form
        return context

    def get_queryset(self):
        return Review.objects.filter(is_published=True)
