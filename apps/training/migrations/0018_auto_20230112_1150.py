# Generated by Django 3.2.16 on 2023-01-12 08:50

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0017_traininguser_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='traininguser',
            name='antrenman',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='Antrenman Açıklaması'),
        ),
        migrations.AddField(
            model_name='traininguser',
            name='set',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Set Sayısı'),
        ),
    ]
