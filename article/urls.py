from django.urls import path, include
from article import views

api_article_urls = [
    path('create/', views.ArticleCreateAPI.as_view(), name='article_create'),
    path('list/<str:category>/', views.ArticleListAPI.as_view(), name="article_list"),
    path('categories/', views.ArticleCategoriesAPI.as_view(), name='article_categories'),
]

urlpatterns = [
    path('api/v1/articles/', include(api_article_urls), name='article_create')
]
