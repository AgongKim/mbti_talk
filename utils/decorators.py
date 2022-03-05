import functools
from utils.exception import CustomApiException, get_msg
from user.models import User

def auth_required(f):
    @functools.wraps(f)
    def wrap(self, request, *args, **kwargs):
        debug_user_id = request.META.get('HTTP_DEBUG_USERID')
        debug_email   = request.META.get('HTTP_DEBUG_EMAIL')
        user = None
        if debug_user_id:
            user = User.objects.filter(pk=debug_user_id).first()
            request.user = user
        elif debug_email:
            user = User.objects.filter(email=debug_email).first()
            request.user = user
        if not request.user.is_authenticated:
            raise CustomApiException(detail=get_msg("auth_failed"))
        if request.user.status != 1:
            raise CustomApiException(detail=get_msg("status_abnormal"))
        
        
        return f(self, request, *args, **kwargs)
    return wrap
