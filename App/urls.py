from django.urls import path
from . import views
urlpatterns = [
    path('welcome',views.WelcomeAPI.as_view(),name="WelcomeApiView"),
    path('category',views.CategoryAPIView.as_view(),name="CategoryAPIView"),
    path('category/<int:pk>',views.CategoryAPIView.as_view())
]