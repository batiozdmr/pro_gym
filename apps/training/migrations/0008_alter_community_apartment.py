# Generated by Django 3.2.16 on 2023-01-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0007_alter_community_apartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='apartment',
            field=models.IntegerField(blank=True, null=True, verbose_name='Daire'),
        ),
    ]