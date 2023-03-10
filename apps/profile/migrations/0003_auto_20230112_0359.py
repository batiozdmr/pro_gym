# Generated by Django 3.2.16 on 2023-01-12 00:59

import apps.common.fileUpload.userPath
import apps.common.fileUpload.validate
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_delete_phoneauthorizations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='max_credit',
        ),
        migrations.AddField(
            model_name='profile',
            name='qr',
            field=models.ImageField(blank=True, null=True, upload_to=apps.common.fileUpload.userPath.userDirectoryPath, validators=[apps.common.fileUpload.validate.validateFileExtensionPhoto], verbose_name='qr'),
        ),
    ]
