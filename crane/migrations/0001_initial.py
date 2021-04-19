# Generated by Django 3.1.7 on 2021-03-29 08:12

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('descript', models.TextField()),
            ],
            options={
                'db_table': 'type',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=16)),
                ('gender', models.IntegerField(choices=[('1', '男'), ('2', '女')], default=1)),
                ('address', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now=True, verbose_name='日期')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_title', models.CharField(max_length=128, verbose_name='标题')),
                ('art_date', models.DateField(auto_now=True, verbose_name='日期')),
                ('art_content', ckeditor.fields.RichTextField()),
                ('art_des', ckeditor.fields.RichTextField()),
                ('art_recommend', models.IntegerField(default=0, verbose_name='推荐')),
                ('art_click', models.IntegerField(default=0, verbose_name='点击率')),
                ('art_picture', models.ImageField(upload_to='../static/images/')),
                ('art_status', models.IntegerField()),
                ('art_author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='crane.user', verbose_name='作者')),
                ('art_tp', models.ManyToManyField(to='crane.Type')),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]