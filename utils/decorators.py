import functools
from utils.exception import CustomApiException, get_msg

def auth_required(f):
    @functools.wraps(f)
    def wrap(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise CustomApiException(detail=get_msg("auth_failed"))
        if request.user.status != 1:
            raise CustomApiException(detail=get_msg("status_abnormal"))
        return f(self, request, *args, **kwargs)
    return wrap
