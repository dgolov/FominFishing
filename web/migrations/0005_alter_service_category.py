# Generated by Django 4.0.3 on 2022-04-17 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_category_video_service_is_active_service_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.category', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
