from rest_framework import serializers

from blog import models
from blog.models import Subject, Teacher, PrivacyPolicyHistory


##  批量插入数据
from common.utils.exceptions import ParamsIsNullException


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
    def validate(self,validated_data):
        if validated_data.get("account_id")=="cl":
            raise ParamsIsNullException("account_id")
    #重新定义
    def create(self, validated_data):
        return PrivacyPolicyHistory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.account_id = validated_data.get('account_id', instance.account_id)
        instance.type= validated_data.get('type', instance.type)
        instance.version = validated_data.get('version', instance.version)
        instance.save()
        return instance
