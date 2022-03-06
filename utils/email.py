from cgitb import html
from django.core.mail import send_mail as send
from django.conf import settings
from utils.encrypt import email_auth_url_encode

def send_mail(case, recipeint_list, user):
    if case == 'join_auth':
        url = email_auth_url_encode(user)
        send('MBTI TALK 가입 인증 메일입니다.', 'test',\
             settings.EMAIL_HOST_USER,recipeint_list,html_message=url)
