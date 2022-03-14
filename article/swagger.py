from drf_yasg.openapi import Parameter, IN_QUERY
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class ArticleCreateSwagger:
    params = {
        "category": openapi.Schema(type=openapi.TYPE_STRING, description='게시글 카테고리'),
        "title": openapi.Schema(type=openapi.TYPE_STRING, description='게시글 제목'),
        "contents": openapi.Schema(type=openapi.TYPE_STRING, description='게시글 내용'),
    }

    req = openapi.Schema(type=openapi.TYPE_OBJECT, properties=params,required=["category", "title"])

    res = {
           "200": openapi.Response(
                description="성공",
                examples={
                    "application/json": {
                        "gcode": 0,
                        "success": True,
                        "data" : "<articledata>"
                    }
                }
            )
        }

class ArticleListSwagger:
    params = [
        Parameter('offset', IN_QUERY,type=openapi.TYPE_INTEGER,description='페이지'),
        Parameter('limit', IN_QUERY,type=openapi.TYPE_INTEGER,description='페이지에 게시글 수'),
    ]
    res ={
        "200" : openapi.Response(
            description="성공",
            examples={
                "application/json": {
                    "gcode": 0,
                    "success": True,
                    "total_count": 20,
                    "count":9999,
                    "data" : ["<articledata>"]
                }
            }
        )
    } 
    
swagger_article_create = swagger_auto_schema(operation_summary='[유저트큰 필요] 게시글 작성 api', request_body=ArticleCreateSwagger.req, responses=ArticleCreateSwagger.res)
swagger_article_list = swagger_auto_schema(operation_summary="[유저토큰 필요] 게시글 불러오기 api", manual_parameters=ArticleListSwagger.params,responses=ArticleListSwagger.res)