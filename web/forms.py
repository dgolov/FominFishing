from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Request, Service


class RequestForm(forms.ModelForm):
    """ Форма регистрации нового контракта в CRM
    """
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control common-input mb-20', 'placeholder': 'Укажите ваше имя'}
        )
    )
    service = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control mb-20'}
        )
    )
    date = forms.DateField(
        widget=AdminDateWidget(
            attrs={'class': 'form-control common-input mb-20', 'type': "date"}
        )
    )
    email = forms.EmailField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control common-input mb-20', 'placeholder': 'Укажите email'}
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control common-input mb-20', 'placeholder': 'Укажите номер телефона'}
        )
    )
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control common-textarea mt-10 ',
                'placeholder': 'Ваше сообщение',
                'style': 'height: 200px;'
            }
        )
    )

    class Meta:
        model = Request
        fields = ('name', 'service', 'date', 'email', 'phone', 'comment')
