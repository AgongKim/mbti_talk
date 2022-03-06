from django.urls import path, include
from user import views

api_user_urls = [
    path('create/', views.UserCreateAPI.as_view(), name='user_create'),
    path('delete/', views.UserDeleteAPI.as_view(), name='user_delete'),
    path('update/', views.UserUpdateAPI.as_view(), name='user_update'),
    path('detail/', views.UserDetailAPI.as_view(), name='user_detail'),
    path('mail_auth/<str:_encoded>/', views.UserEmailAuthAPI.as_view(), name='user_email_auth'),
]

urlpatterns = [
    path('api/v1/users/', include(api_user_urls))
]