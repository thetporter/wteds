# Generated by Django 5.1.3 on 2024-12-15 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_merch_alter_singlepost_creation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='merch',
            name='favof',
            field=models.ManyToManyField(blank=True, null=True, to='app.userexpanded', verbose_name='В избранном у'),
        ),
        migrations.AddField(
            model_name='userexpanded',
            name='favs',
            field=models.ManyToManyField(blank=True, to='app.merch'),
        ),
        migrations.AlterField(
            model_name='order',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 15, 13, 24, 17, 479458), verbose_name='Создание'),
        ),
        migrations.AlterField(
            model_name='singlepost',
            name='creation_date',
            field=models.DateField(db_index=True, default=datetime.datetime(2024, 12, 15, 13, 24, 17, 477465), editable=False, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='active',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 15, 13, 24, 17, 478462), verbose_name='Последняя активность'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 15, 13, 24, 17, 478462), verbose_name='Создание'),
        ),
        migrations.AlterField(
            model_name='threadcomment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 15, 13, 24, 17, 478462), verbose_name='Создание'),
        ),
    ]