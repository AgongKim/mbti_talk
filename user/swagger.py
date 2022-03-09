from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class UserCreateSwagger:
    params = {
        "email": openapi.Schema(type=openapi.TYPE_STRING, description='user_email'),
        "password": openapi.Schema(type=openapi.TYPE_STRING, description='user_password'),
        "nickname": openapi.Schema(type=openapi.TYPE_STRING, description='user_nickname'),
    }

    req = openapi.Schema(type=openapi.TYPE_OBJECT, properties=params)

    res = {
        "201": openapi.Response(
            description="가입 성공",
            examples={
                "application/json": {
                    "gcode": 0,
                    "success": True,
                }
            },
        ),
        "400": openapi.Response(
            description="부적절한 형태의 파라미터",
            examples={
                "application/json": {
                    "gcode": 9000,
                    "msg": "INVALID_FORMAT",
                    "success": False,
                }
            },
        ),
    }

swagger_user_create = swagger_auto_schema(request_body=UserCreateSwagger.req, responses=UserCreateSwagger.res)