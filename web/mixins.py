import logging

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import HttpResponseRedirect
from .forms import RequestForm


logger = logging.getLogger(__name__)


class FormMixin:
    """ Миксин для отправки заявок
    """
    success_form_url = ''
    form = RequestForm()

    def post(self, request, *args, **kwargs):
        logger.debug('[SendRequest] try to send request')
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('[SendRequest] Send request successfully')
            messages.add_message(
                request,
                messages.SUCCESS,
                'Спасибо за заявку! В близжайшее время я свяжусь с Вами!'
            )
            try:
                logger.debug('[SendRequest] try to send mail')
                send_mail(
                    'Заявка на сайте',
                    'Отправлена заявка на сайте av-fomin.ru!',
                    'myvmeste_info@mail.ru',
                    ['dgolov@icloud.com'],
                    fail_silently=False
                )
            except Exception as e:
                logger.error(f'[SendRequest] Send message fail: {e}')
            return HttpResponseRedirect(f'/{self.success_form_url}#contact')
        messages.add_message(request, messages.ERROR, 'Произошла ошибка! Попробуйте повторить запрос позже.')
        logger.error(f'[SendRequest] Send request fail')
        return HttpResponseRedirect(f'/')
