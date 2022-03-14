from django.http import JsonResponse
from utils.messages import get_msg


class FailResponse(JsonResponse):
    def __init__(self, msg):
        res = {
            "status" : "500",
            "gcode" : "9000",
            "detail" : msg
        }
        super().__init__(res,status=500)

class SuccessResponse(JsonResponse):
    def __init__(self, data={}):
        res = {
            "status" : 200,
            "gcode" : "0",
            "data" : data
        }
        super().__init__(res,status=200)
