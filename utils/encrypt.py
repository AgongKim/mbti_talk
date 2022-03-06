import imp
from django.conf import settings
from user.models import User
import base64
import hashlib

def email_auth_url_encode(user):
    url = settings.HOST_DOMAIN + "api/v1/users/mail_auth/"
    _code = f"{user.email}:{user.date_joined}"
    _encoded = base64.urlsafe_b64encode(_code.encode('utf-8'))
    url = url + _encoded.decode('utf-8')
    return url

def email_auth_user(_encoded):
    _encoded = base64.urlsafe_b64decode(_encoded.encode('utf-8')).decode('utf-8')
    user_email = _encoded.split(":")[0]
    user = User.objects.get(email=user_email)
    return user
