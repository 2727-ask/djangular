from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from . import views
urlpatterns = [
    path('welcome',views.WelcomeAPI.as_view(),name="WelcomeApiView"),
    path('category',views.CategoryAPIView.as_view(),name="CategoryAPIView"),
    path('category/<int:pk>',views.CategoryAPIView.as_view()),
    path('auth-jwt',obtain_jwt_token),
    path('refresh-jwt', refresh_jwt_token),
    path('verify-jwt',verify_jwt_token)
]