from rest_framework.exceptions import APIException
from utils.messages import get_msg

class CustomApiException(APIException):
    def __init__(self, **kwargs):
        self.status_code = kwargs.get("status", 400)
        self.gcode = kwargs.get("gcode", 9000)
        self.detail = kwargs.get("detail", "알 수 없는 오류가 발생했습니다.")