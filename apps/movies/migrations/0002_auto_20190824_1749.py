# Generated by Django 2.2.4 on 2019-08-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='user_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='top',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user_favorite',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
