import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer
from utils.responses import FailResponse, SuccessResponse, get_msg
from django.contrib.auth.hashers import make_password
from utils.decorators import auth_required
from utils.encrypt import email_auth_user
from django.core.exceptions import ObjectDoesNotExist
from user.swagger import *
from django.db.models import Q

class UserCreateAPI(APIView):
    swagger_tags = ['users']

    @swagger_user_create
    def post(self, request):
        try:
            _data = json.loads(request.body)
            #validate data
            if not _data.get('password') or not _data.get('email') or not _data.get('mbti'):
                return FailResponse(get_msg("parameter_missing"))
            if User.objects.filter(Q(email=_data['email']) | Q(nickname=_data['nickname'])).exists():
                return FailResponse(get_msg("duplicate_field"))
            
            _data['password'] = make_password(_data['password'])
            u = User.objects.create(**_data)
            # auth mail send
            def send_signup_email():
                from utils import email
                email.send_mail('join_auth', [u.email], u)
            import threading
            t = threading.Thread(target=send_signup_email)
            t.start()
            
            return SuccessResponse(UserSerializer(u).data)

        except Exception as e:
            print(e)
            return FailResponse(get_msg("invalid_format"))

class UserUpdateAPI(APIView):
    swagger_tags = ['users']

    @auth_required
    @swagger_user_update
    def post(self, request):
        try:
            _data = json.loads(request.body)
            #validate data
            if _data.get('email'):
                return FailResponse(get_msg('cant_change_email'))
            if _data.get('password'):
                _data['password'] = make_password(_data['password'])

            u = request.user
            if _data['password']:
                u.password = _data['password']
            elif _data['nickname']:
                u.nickname = _data['nickname']
            u.save()

            return SuccessResponse(UserSerializer(u).data)
        except:
            return FailResponse(get_msg("invalid_format"))


class UserDeleteAPI(APIView):
    swagger_tags = ['users']

    @auth_required
    @swagger_user_delete
    def post(self, request):
        user = request.user
        user.status = 999
        user.is_active = False
        user.save()
        return SuccessResponse()


class UserDetailAPI(APIView):
    swagger_tags = ['users']

    @auth_required
    @swagger_user_detail
    def get(self, request):
        return SuccessResponse(UserSerializer(request.user).data)


class UserEmailAuthAPI(APIView):
    swagger_tags = ['users']
    
    @swagger_email_auth
    def get(self, request, _encoded):
        try:
            user = email_auth_user(_encoded)
        except ObjectDoesNotExist:
            return FailResponse(get_msg("email_not_exists"))
        user.status = 1
        user.save()
        return SuccessResponse(UserSerializer(user).data)
