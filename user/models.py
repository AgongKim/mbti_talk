
from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import UserManager

class User(AbstractUser):
    DOMAIN_CHOICE = (
        ('EM','email'),
        ('GO','google'),
        ('KA','kakao')
    )
    objects = UserManager()
    
    username = None
    first_name = None
    last_name = None
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=100)
    domain = models.CharField(max_length=2, choices=DOMAIN_CHOICE, default='EM')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True)

    class Meta:
        db_table = 'app_user'
        app_label = 'user'
    
    def __str__(self):
        return self.email