# Generated by Django 5.1.3 on 2024-12-15 10:18

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_singlepost_image_1_singlepost_image_2_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Merch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('image_1', models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Картинка (1)')),
                ('image_2', models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Картинка (2)')),
                ('image_3', models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Картинка (3)')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'db_table': 'merch_items',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='singlepost',
            name='creation_date',
            field=models.DateField(db_index=True, default=datetime.datetime(2024, 12, 15, 13, 18, 24, 404536), editable=False, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='singlepost',
            name='image_1',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Картинка (1)'),
        ),
        migrations.AlterField(
            model_name='singlepost',
            name='image_2',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Картинка (2)'),
        ),
        migrations.AlterField(
            model_name='singlepost',
            name='image_3',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Картинка (3)'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='active',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 15, 13, 18, 24, 404536), verbose_name='Последняя активность'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 15, 13, 18, 24, 404536), verbose_name='Создание'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='threadcomment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 15, 13, 18, 24, 404536), verbose_name='Создание'),
        ),
        migrations.AlterField(
            model_name='threadcomment',
            name='image_1',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Картинка (1)'),
        ),
        migrations.AlterField(
            model_name='threadcomment',
            name='image_2',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Картинка (2)'),
        ),
        migrations.AlterField(
            model_name='threadcomment',
            name='image_3',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Картинка (3)'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('totalcost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итого')),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2024, 12, 15, 13, 18, 24, 405533), verbose_name='Создание')),
                ('status', models.CharField(choices=[('AS', 'Собирается'), ('SE', 'Отправлен'), ('AR', 'Прибыл')], db_default='AS', default='Собирается', max_length=32, verbose_name='')),
                ('merch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.merch', verbose_name='Товары')),
                ('placed_by', models.ForeignKey(default='Удаленный пользователь', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'db_table': 'orders',
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='UserExpanded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.BooleanField(verbose_name='Менеджер')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'дополнение пользователя',
                'verbose_name_plural': 'дополнения',
            },
        ),
    ]
