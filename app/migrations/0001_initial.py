# Generated by Django 5.0.4 on 2024-04-30 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SinglePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('short_desc', models.CharField(blank=True, max_length=512, null=True, verbose_name='Краткое описание')),
                ('text', models.TextField(verbose_name='Основной текст')),
                ('creation_date', models.DateField(db_index=True, default=datetime.datetime(2024, 4, 30, 18, 23, 7, 730482), editable=False, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'одиночная публикация',
                'verbose_name_plural': 'одиночные публикации',
                'db_table': 'single_posts',
                'ordering': ['-creation_date', 'title'],
            },
        ),
    ]
