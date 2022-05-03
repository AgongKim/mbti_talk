import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from utils.responses import FailResponse, SuccessResponse, get_msg
from utils.decorators import auth_required
from mbti_talk.configs import MBTI_LIST, BOARD_CATEGORIES
from article.models import Article, Comment
from article.serializers import ArticleSerializer,CommentSerializer
from article.swagger import *
from django.core.paginator import Paginator

class ArticleCreateAPI(APIView):
    swagger_tags = ['article']

    
    @auth_required
    @swagger_article_create
    def post(self, request):
        try:
            _data = json.loads(request.body)
            if not _data.get('category') or not _data.get('title'):
                return FailResponse(get_msg("parameter_missing"))
            if ( _data.get('category') not in MBTI_LIST and \
                    _data.get('category') != 'FREE' ) or \
                    ( _data.get('category') in MBTI_LIST and \
                        _data.get('category') != request.user.mbti ):
                return FailResponse(get_msg("invalid_category"))
            if _data.get('hits'):
                return FailResponse(get_msg("no_hits_control"))
            _data["author"] = request.user

            article = Article.objects.create(**_data)
            return SuccessResponse(ArticleSerializer(article).data)
        except Exception as e:
            print(e)
            return FailResponse(get_msg("invalid_format"))


class ArticleListAPI(APIView):
    swagger_tags = ['article']


    @auth_required
    @swagger_article_list
    def get(self, request, category):
        offset = request.GET.get('offset', 1)
        limit = request.GET.get('limit', 20)
        total_list = Article.objects.filter(category=category).order_by('-created_at')
        paginator = Paginator(total_list,limit)
        cutoff_list = paginator.get_page(offset)

        total_count = total_list.count()
        count = len(cutoff_list)
        
        result = {}
        result['status'] = 200
        result['gcode'] = 0
        result['total_count'] = total_count
        result['count'] = count
        result['data'] = ArticleSerializer(cutoff_list, many=True).data
        
        return JsonResponse(result)

class ArticleDetailAPI(APIView):
    swagger_tags = ['article']
    def get(self, request, article_id):
        try:
            article = Article.objects.get(id=article_id)
            comment = Comment.objects.filter(article_id=article_id)
            result = {}
            result['status'] = 200
            result['gcode'] = 0
            data = ArticleSerializer(article, many=False).data
            data['comment'] = CommentSerializer(comment, many=True).data
            result['data'] = data
            return JsonResponse(result)
        except Exception as e:
            print(e)
            return FailResponse(get_msg("invalid_format")) 

class ArticleCategoriesAPI(APIView):
    swagger_tags = ['category']
    
    def get(self,request):
        from mbti_talk.configs import BOARD_CATEGORIES
        data = [i[0] for i in BOARD_CATEGORIES]
        result = {}
        result['status'] = 200
        result['gcode'] = 0
        result['data'] = data
        return JsonResponse(result)
    

class ArticleLikeAPI(APIView):
    swagger_tags = ['article']

    @auth_required
    def post(self, request):
        try:
            _data = json.loads(request.body)
            article_id = _data.get('article_id')
             
        except Exception as e:
            print(e)
            return FailResponse(get_msg("invalid_format"))

class CommentCreateAPI(APIView):
    swagger_tags = ['comment']

    @auth_required
    @swagger_comment_create
    def post(self, request):
        try:
            _data = json.loads(request.body)
            if not _data.get('article_id'):
                return FailResponse(get_msg("parameter_missing"))
            _data["author"] = request.user 
            comment = Comment.objects.create(**_data)
            return SuccessResponse(CommentSerializer(comment).data)
        except Exception as e:
            print(e)
            return FailResponse(get_msg("invalid_format"))
