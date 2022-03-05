import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer
from utils.exception import CustomApiException, get_msg
from django.contrib.auth.hashers import make_password
from utils.decorators import auth_required

# Create your views here.
class UserCreateAPI(APIView):
    def post(self, request):
        _data = json.loads(request.body)
        print(_data)
        if not _data.get('password') or not _data.get('email'):
            raise CustomApiException(detail=get_msg('parameter_missing'))
        if User.objects.filter(email=_data.get('email')).exists():
            raise CustomApiException(detail="email_already_exists")
        pwd = _data.pop('password')
        pwd = make_password(pwd)
        _data['password'] = pwd
        serializer = UserSerializer(data=_data)
        if not serializer.is_valid():
            raise CustomApiException(detail=get_msg('parameter_missing'))
        u = User.objects.create(**_data)
        return Response(serializer.data)


class UserUpdateAPI(APIView):
    @auth_required
    def post(self, request):
        data = json.loads(request.body)
        #validate ds

        u = request.user
        for attr, value in data.items():
            setattr(u, attr, value)
            u.save()
        return JsonResponse({'status':200,'result':'test'})



class UserDeleteAPI(APIView):
    def get(self, request):
        return JsonResponse({'status':200,'result':'test'})


class UserDetailAPI(APIView):
    def get(self, request):
        return JsonResponse({'status':200,'result':'test'})