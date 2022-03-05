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
        try:
            _data = json.loads(request.body)
            print(_data)
            if not _data.get('password') or not _data.get('email'):
                raise CustomApiException(detail=get_msg('parameter_missing'))
            if User.objects.filter(email=_data.get('email')).exists():
                raise CustomApiException(detail="email_already_exists")
            pwd = _data.pop('password')
            pwd = make_password(pwd)
            _data['password'] = pwd
            u = User.objects.create(**_data)
            return Response(UserSerializer(u).data)
        except TypeError:
            raise CustomApiException(detail="invalid_format")


class UserUpdateAPI(APIView):
    @auth_required
    def post(self, request):
        try:
            _data = json.loads(request.body)
            if _data.get('email'):
                raise CustomApiException(detail=get_msg('cant_change_email'))
            #validate data

            u = request.user
            for attr, value in _data.items():
                setattr(u, attr, value)
                u.save()
            return Response(UserSerializer(u).data)
        except TypeError:
            raise CustomApiException(detail="invalid_format")


class UserDeleteAPI(APIView):
    def get(self, request):
        return JsonResponse({'status':200,'result':'test'})


class UserDetailAPI(APIView):
    @auth_required   
    def get(self, request):
        return Response(UserSerializer(request.user).data)