# Generated by Django 3.2.16 on 2023-01-12 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0014_auto_20230105_1255'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InterviewStatus',
            new_name='TrainingUser',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='community',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='interview_status',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='traininguser',
            options={'default_permissions': (), 'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')), 'verbose_name': 'Eğitimler', 'verbose_name_plural': 'Eğitimler'},
        ),
        migrations.DeleteModel(
            name='Community',
        ),
        migrations.DeleteModel(
            name='Interview',
        ),
    ]
