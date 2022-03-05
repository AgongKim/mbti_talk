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
        data = json.loads(request.body)
        if not data.get('password') or not data.get('email'):
            raise CustomApiException(detail=get_msg('parameter_missing'))
        if User.objects.filter(email=data.get('email')).exists():
            raise CustomApiException(detail="email_already_exists")
        pwd = data.pop('password')
        pwd = make_password(pwd)
        data['password'] = pwd
        u = User.objects.create(**data)
        data = UserSerializer(u).data
        return Response(data)


class UserUpdateAPI(APIView):
    @auth_required
    def get(self, request):
        return JsonResponse({'status':200,'result':'test'})



class UserDeleteAPI(APIView):
    def get(self, request):
        return JsonResponse({'status':200,'result':'test'})


class UserDetailAPI(APIView):
    def get(self, request):
        return JsonResponse({'status':200,'result':'test'})