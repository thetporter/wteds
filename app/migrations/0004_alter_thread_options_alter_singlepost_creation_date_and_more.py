# Generated by Django 5.0.4 on 2024-04-30 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_singlepost_creation_date_thread_threadcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-active', '-created'], 'verbose_name': 'форумная публикация', 'verbose_name_plural': 'форумные публикации'},
        ),
        migrations.AlterField(
            model_name='singlepost',
            name='creation_date',
            field=models.DateField(db_index=True, default=datetime.datetime(2024, 4, 30, 23, 0, 25, 664124), editable=False, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='active',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 30, 23, 0, 25, 665120), verbose_name='Последняя активность'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 30, 23, 0, 25, 665120), verbose_name='Создание'),
        ),
        migrations.AlterField(
            model_name='threadcomment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 30, 23, 0, 25, 665120), verbose_name='Создание'),
        ),
    ]