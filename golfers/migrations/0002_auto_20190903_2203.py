# Generated by Django 2.2.4 on 2019-09-03 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golfer',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='golfer',
            name='identifier',
            field=models.CharField(max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='comment',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
