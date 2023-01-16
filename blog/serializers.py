from rest_framework import serializers

from blog import models
from blog.models import Subject, Teacher, PrivacyPolicyHistory


##  批量插入数据
class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
        # 当有表关联时指定数据库表级联查询的层级，不指定默认不会进行级联查询
        depath = 1

class BookmodelPartSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    intro = serializers.CharField(max_length=1000)

    class Meta:
        model = Subject
        fields =('name','intro')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields = "__all__"
        # 当有表关联时指定数据库表级联查询的层级，不指定默认不会进行级联查询

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicyHistory
        fields = "__all__"