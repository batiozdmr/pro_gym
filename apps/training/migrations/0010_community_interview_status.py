# Generated by Django 3.2.16 on 2023-01-01 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0009_alter_community_m2'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='interview_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_interview_status', to='training.interviewstatus', verbose_name='Durum'),
        ),
    ]
