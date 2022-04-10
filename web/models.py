from django.db import models


class Service(models.Model):
    """ Модели услуги
    """
    name = models.CharField(max_length=100, verbose_name='Наименование услуги')
    slug = models.CharField(max_length=100, verbose_name='Ссылка')
    description = models.TextField(verbose_name='Описание услуги')
    photo = models.ImageField(upload_to='service', verbose_name='Фотография')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name='Цена', blank=True, null=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class Photo(models.Model):
    """ Модели фотографии
    """
    short_description = models.CharField(max_length=100, verbose_name='Краткое описание')
    path = models.ImageField(upload_to='photos', verbose_name='Фотография')
    in_main_page = models.BooleanField(default=False, verbose_name='На главной странице')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.short_description


class Request(models.Model):
    """ Модели заявки
    """
    name = models.CharField(max_length=150, verbose_name='ФИО')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, verbose_name='Услуга', null=True)
    date = models.DateField(verbose_name='Дата рыбалки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')
    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    comment = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявка'

    def __str__(self):
        return self.name


class Review(models.Model):
    """ Модели отзыва
    """
    name = models.CharField(max_length=150, verbose_name='ФИО')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва')
    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True)
    comment = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name
