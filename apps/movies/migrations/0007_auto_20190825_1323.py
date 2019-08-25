# Generated by Django 2.2.4 on 2019-08-25 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20190825_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='actor',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='comments_num',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='country',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='director',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='image',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='image_path',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='movie_type',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='play_able',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='star',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='top',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='year',
            field=models.CharField(blank=True, default='', max_length=60, null=True),
        ),
    ]
