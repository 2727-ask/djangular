from django.urls import path
from . import views
urlpatterns = [
    path('category',views.CategoryAPIView.as_view(),name="CategoryAPIView"),
    path('category/<int:pk>',views.CategoryAPIView.as_view())
]