from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from .Views import categoryAPIView
urlpatterns = [
    path('category',categoryAPIView.CategoryAPIView.as_view(),name="categoryAPIView.py"),
    path('category/<int:pk>',categoryAPIView.CategoryAPIView.as_view()),
    path('auth-jwt',obtain_jwt_token),
    path('refresh-jwt', refresh_jwt_token),
    path('verify-jwt',verify_jwt_token)
]