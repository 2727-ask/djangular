from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from .Views import categoryAPIView, blogpostAPIView, signUpAPIView,profileAPIView, verifyEmailAPIView, forgotPasswordAPIView, changePasswordAPIView
urlpatterns = [
    path('category',categoryAPIView.CategoryAPIView.as_view(),name="categoryAPIView.py"),
    path('category/<int:pk>',categoryAPIView.CategoryAPIView.as_view()),
    path('api/blog_post/',blogpostAPIView.BlogPostAPIView.as_view()),
    path('api/signup/',signUpAPIView.SignUpAPIView.as_view()),
    path('api/profile/',profileAPIView.ProfileAPIView.as_view()),
    path('api/forgotPassword/',forgotPasswordAPIView.ForgotPasswordAPIView.as_view()),
    path('api/verifyEmail/',verifyEmailAPIView.VerifyEmailAPIView.as_view()),
    path('api/auth-jwt',obtain_jwt_token),
    path('refresh-jwt', refresh_jwt_token),
    path('verify-jwt',verify_jwt_token)
]