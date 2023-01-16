import json
from random import sample

from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render, redirect
# Create your views here.
from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from blog.models import Subject, Teacher, PrivacyPolicyHistory
from rest_framework.views import APIView, Response
from blog.models import Subject
from common.utils.generic import response_success
from .serializers import BookModelSerializer, TeacherSerializer, BookmodelPartSerializer, PolicySerializer


class SubjectsView(APIView):
    def get(self, request):
        name = request.GET.get("name")
        print(name)
        subjects = (Subject.objects.filter(name=name).all())
        res = []
        for subject in subjects:
            res.append(
                {
                    "intro": model_to_dict(subject).get("intro"),
                }
            )
        print(res)
        return HttpResponse(json.dumps(res))
    ##


    ## 插入一个数据就
    def post(self, request, *args, **kwargs):
        data=request.data
        result=[]
        book_data={}
        for in_data in data:
            result.append(
                {
                  'name': in_data.get('name'),
                  'intro': in_data.get('intro'),
                }
            )

        subject_ser = BookmodelPartSerializer(data=result, many=True)
        if subject_ser.is_valid(raise_exception=True):
            subject_ser.save()
            return Response(subject_ser.data)

    def put(self, request, *args, **kwargs):
            request_data = request.data
            if kwargs.get("pk"):
                book =Subject.objects.get(id=kwargs.get("pk"))
                book_ser = BookModelSerializer(instance=book, data=request_data)
                if book_ser.is_valid(raise_exception=True):
                    book_ser.save()
                    return Response(book_ser.data)


    def delete(self, request, *args, **kwargs):
        if kwargs.get("pk", None):
            Subject.objects.get(id=kwargs.get("pk")).delete()
            return Response()


class TeachersView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        res = []
        for t in teachers:
            res.append(model_to_dict(t)
            )
        print(res)
        return HttpResponse(json.dumps(res))

class PolicyView(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          generics.GenericAPIView):
    queryset = PrivacyPolicyHistory.objects.all()
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    parser_classes = (JSONParser,)
    serializer_class = PolicySerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        #policy = PrivacyPolicyHistory.objects.latest('id')
        #serializers = self.get_serializer(policy)
        return self.retrieve(request, *args, **kwargs)

    ##直接用post方法插入数据
    def post(self, request):
        data = request.data
        print("the post data is %s" % data)
        policy_ser = self.get_serializer(data=data)
        policy_ser.is_valid(raise_exception=True)
        policy_ser.save()
        return response_success(policy_ser.data)

    ##在serializer中定义了update方法，直接用put方法更新数据
    def put(self, request, *args, **kwargs):
        request_data = request.data
        if kwargs.get("id"):
            policy = self.get_object()
            policy_ser = self.get_serializer(instance=policy, data=request_data)
            print("the policy_ser is %s" % policy_ser)
            if policy_ser.is_valid(raise_exception=True):
                policy_ser.save()
                print("the policy_ser is %s" % policy_ser)
                return response_success(policy_ser.data)
        return response_success("error")

class GetAllPolicyView(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          generics.GenericAPIView):
    queryset = PrivacyPolicyHistory.objects.all()
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    parser_classes = (JSONParser,)
    serializer_class = PolicySerializer
    def get(self,request):
        instance = self.get_queryset()
        print("the all data is %s",instance)
        serializer = PolicySerializer(instance=instance, many=True)
        return response_success(serializer.data)


