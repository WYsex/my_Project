from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

gender_list=[
    (1,"男"),
    (2,"女")
]

class User(models.Model):
    username=models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=16)
    gender = models.IntegerField(choices=gender_list, default=1)
    address = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now=True, verbose_name='日期')

    class Meta:
        db_table = "user"

class Type(models.Model):
    name=models.CharField(max_length=32)
    descript=models.TextField()

    class Meta:
        db_table='type'

class Article(models.Model):
    art_title=models.CharField(max_length=128,verbose_name='标题')
    art_date=models.DateField(auto_now=True,verbose_name='日期')
    art_content=RichTextField()
    art_des=RichTextField()
    #推荐
    art_recommend=models.IntegerField(default=0,verbose_name='推荐')
    #点击率
    art_click=models.IntegerField(default=0,verbose_name='点击率')
    art_picture=models.ImageField(upload_to='../static/images/')
    art_author=models.ForeignKey(to=User,on_delete=models.SET_DEFAULT,default=1,verbose_name='作者')
    art_tp=models.ManyToManyField(to=Type)
    art_status=models.IntegerField()

    def __str__(self):
        return self.art_title

    class Meta:
        db_table = "article"
