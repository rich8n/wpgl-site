# Generated by Django 2.2.4 on 2019-09-03 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfers', '0002_auto_20190903_2203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('-bye_team', 'team_name')},
        ),
    ]
