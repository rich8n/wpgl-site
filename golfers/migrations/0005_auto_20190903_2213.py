# Generated by Django 2.2.4 on 2019-09-03 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfers', '0004_auto_20190903_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golfer',
            name='suffix',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]