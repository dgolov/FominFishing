from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from .forms import RequestForm


class FormMixin:
    """ Миксин для отправки заявок
    """
    success_form_url = ''
    form = RequestForm()

    def post(self, request, *args, **kwargs):
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Спасибо за заявку! В близжайшее время я свяжусь с Вами!.'
            )
            return HttpResponseRedirect(f'/{self.success_form_url}#contact')
