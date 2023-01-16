import time

from django.db import models

# Create your models here.
class BlogModel(models.Model):
    #在django中会默认生成可以不用写这行
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    class Meta():
        db_table = 'bolog'

class Subject(models.Model):
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=50, verbose_name='名称')
    intro = models.CharField(max_length=1000, verbose_name='介绍')
    is_hot = models.BooleanField(verbose_name='是否热门',null=True)
    class Meta:
        db_table = 'tb_subject'
        verbose_name = '学科'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class Teacher(models.Model):
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=20, verbose_name='姓名')
    sex = models.BooleanField(default=True, verbose_name='性别')
    birth = models.IntegerField(verbose_name='出生日期')
    intro = models.CharField(max_length=1000, verbose_name='个人介绍')
    photo = models.CharField(max_length=255, verbose_name='照片')
    good_count = models.IntegerField(default=0, db_column='gcount', verbose_name='好评数')
    bad_count = models.IntegerField(default=0, db_column='bcount', verbose_name='差评数')
    subject = models.ForeignKey(Subject, models.DO_NOTHING, db_column='sno')

    class Meta:
        db_table = 'tb_teacher'
        verbose_name = '教师'
        verbose_name_plural = verbose_name

class PrivacyPolicyHistory(models.Model):
    account_id = models.CharField(max_length=40)
    type = models.CharField(max_length=100)
    version = models.CharField(max_length=40)
    create_time = models.BigIntegerField(default=time.time())

    class Meta:
        db_table = 'privacy_policy_history'
