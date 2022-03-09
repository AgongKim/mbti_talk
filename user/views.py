import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer
from utils.exception import CustomApiException, get_msg
from django.contrib.auth.hashers import make_password
from utils.decorators import auth_required
from utils.encrypt import email_auth_user
from django.core.exceptions import ObjectDoesNotExist
from user.swagger import (
    swagger_user_create,
)

class UserCreateAPI(APIView):
    swagger_tags = ['users']

    @swagger_user_create
    def post(self, request):
        try:
            _data = json.loads(request.body)
            #validate data
            if not _data.get('password') or not _data.get('email'):
                raise CustomApiException(detail=get_msg('parameter_missing'))
            if User.objects.filter(email=_data.get('email')).exists():
                raise CustomApiException(detail="email_already_exists")

            pwd = _data.pop('password')
            pwd = make_password(pwd)
            _data['password'] = pwd
            u = User.objects.create(**_data)
            # auth mail send
            from utils import email
            email.send_mail('join_auth', [u.email], request.user)

            return Response(UserSerializer(u).data)
        except:
            raise CustomApiException(detail='INVALID_FORMAT')

class UserUpdateAPI(APIView):
    @auth_required
    def post(self, request):
        try:
            _data = json.loads(request.body)
            #validate data
            if _data.get('email'):
                raise CustomApiException(detail=get_msg('cant_change_email'))
            if _data.get('password'):
                pwd = _data.pop('password')
                pwd = make_password(pwd)
                _data['password'] = pwd

            u = request.user
            for attr, value in _data.items():
                setattr(u, attr, value)
                u.save()
            return Response(UserSerializer(u).data)
        except:
            raise CustomApiException(detail='INVALID_FORMAT')


class UserDeleteAPI(APIView):
    def get(self, request):
        return JsonResponse({'status':200,'result':'test'})


class UserDetailAPI(APIView):
    @auth_required   
    def get(self, request):
        return Response(UserSerializer(request.user).data)


class UserEmailAuthAPI(APIView):
    def get(self, request, _encoded):
        try:
            user = email_auth_user(_encoded)
        except ObjectDoesNotExist:
            raise CustomApiException(detail="email_not_exists")
        user.status = 1
        user.save()
        return Response(UserSerializer(user).data)
