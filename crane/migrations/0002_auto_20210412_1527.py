# Generated by Django 3.1.7 on 2021-04-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crane', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(1, '男'), (2, '女')], default=1),
        ),
    ]
