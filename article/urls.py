from django.urls import path, include
from article import views

api_article_urls = [
    path('create/', views.ArticleCreateAPI.as_view(), name='article_create'),
    path('list/<str:category>/', views.ArticleListAPI.as_view(), name="article_list"),
    path('categories/', views.ArticleCategoriesAPI.as_view(), name='article_categories'),
    path('detail/<int:article_id>/', views.ArticleDetailAPI.as_view(), name='article_detail'),
]
api_comment_urls = [
    path('create/', views.CommentCreateAPI.as_view(), name='comment_create')
]

urlpatterns = [
    path('api/v1/articles/', include(api_article_urls), name='article_create'),
    path('api/v1/comments/', include(api_comment_urls), name='comment_create')
]
