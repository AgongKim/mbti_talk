from django.contrib.auth.base_user import BaseUserManager
from utils.messages import get_msg

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(get_msg('no_email'))
        email = self.normailize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.full_clean()
        user.save()

        return user

    def instance(self, user):
        # This method is called when `user` is request.user
        return self.get(email=user.email)

    def authenticate(self, user, password):
        return user.check_password(password)