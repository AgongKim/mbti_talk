from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

def Response_with_example(data):
    res = openapi.Response(
            description="성공",
            examples={
                "application/json": {
                    "gcode": 0,
                    "success": True,
                    "data" : data
                }
            }
        )
    return res

class UserCreateSwagger:
    params = {
        "email": openapi.Schema(type=openapi.TYPE_STRING, description='user_email'),
        "password": openapi.Schema(type=openapi.TYPE_STRING, description='user_password'),
        "nickname": openapi.Schema(type=openapi.TYPE_STRING, description='user_nickname'),
        "mbti": openapi.Schema(type=openapi.TYPE_STRING, description='user_mbti(ALL_IN_UPPER_CASE)')
    }

    req = openapi.Schema(type=openapi.TYPE_OBJECT, properties=params,required=["email", "password", "mbti"])

    res = {
        "200": Response_with_example('<userdata>')
    }

class UserUpdateSwagger:
    params = {
        "password": openapi.Schema(type=openapi.TYPE_STRING, description='user_password'),
        "nickname": openapi.Schema(type=openapi.TYPE_STRING, description='user_nickname'),
        "mbti": openapi.Schema(type=openapi.TYPE_STRING, description='user_mbti')
    }
    req = openapi.Schema(type=openapi.TYPE_OBJECT, properties=params)

    res = {
        "200": Response_with_example('<userdata>')
    }

class UserDetailSwagger: 
    res = {
        "200": Response_with_example('<userdata>')
    }

class UserDeleteSwagger:
    params = {}
    req = openapi.Schema(type=openapi.TYPE_OBJECT, properties=params)
    res = {
        "200": Response_with_example("none")
    }

class EmailAuthSwagger:
    res = {
        "200": Response_with_example("<userdata>")
    }
swagger_user_create = swagger_auto_schema(operation_summary='유저 회원가입 api', request_body=UserCreateSwagger.req, responses=UserCreateSwagger.res)
swagger_user_update = swagger_auto_schema(operation_summary='[유저트큰 필요] 유저 정보수정 api', request_body=UserUpdateSwagger.req, responses=UserUpdateSwagger.res)
swagger_user_detail = swagger_auto_schema(operation_summary="[유저토큰 필요] 유저 정보조회 api", responses=UserDetailSwagger.res)
swagger_user_delete = swagger_auto_schema(operation_summary="[유저토큰 필요] 유저 inactive하게 만듬", request_body=UserDeleteSwagger.req, responses=UserDeleteSwagger.res)
swagger_email_auth = swagger_auto_schema(operation_summary="유저 이메일 인증 status를 1로", responses=EmailAuthSwagger.res)