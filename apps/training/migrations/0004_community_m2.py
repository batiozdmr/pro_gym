# Generated by Django 3.2.16 on 2022-12-30 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_community_entrance'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='m2',
            field=models.CharField(max_length=200, null=True, verbose_name='m2'),
        ),
    ]