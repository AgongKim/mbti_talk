from drf_yasg import openapi
from utils.swagger_base import *

swagger_comment_create = PostSwagger(
    params = {
        'article_id': openapi.TYPE_INTEGER,
        'contents': openapi.TYPE_STRING
    },
    required = ["article_id", "contents"],
    description = '[유저토큰 필요] 댓글 작성 api'
).get_auto_schema()
    
swagger_article_create = PostSwagger(
    params = {
        "category": openapi.TYPE_STRING,
        "title": openapi.TYPE_STRING,
        "contents": openapi.TYPE_STRING
    },
    required = ["category", "title"],
    description = '[유저트큰 필요] 게시글 작성 api'
).get_auto_schema()

swagger_article_list = GetSwagger(
    params = {
        'offset': openapi.TYPE_INTEGER,
        'limit': openapi.TYPE_INTEGER,
    },
    examples_={
        "application/json": {
            "gcode": 0,
            "success": True,
            "total_count": 20,
            "count":9999,
            "data" : ["<articledata>"]
        }
    },
    description="[유저토큰 필요] 게시글 불러오기 api"
).get_auto_schema()