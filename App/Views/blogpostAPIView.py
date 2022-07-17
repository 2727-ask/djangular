from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.pagination import PageNumberPagination
from ..models import BlogPost
from ..serializers import BlogPostSerializer


# Create your views here.

class BlogPostAPIView(APIView,PageNumberPagination):
    page_size = 10
    serializer_class = BlogPostSerializer

    def get(self,request,pk=None):
        if(pk):
            query = BlogPostSerializer.objects.filter(id=pk)
            serializer = BlogPostSerializer(query,many=True)
            return Response({"data": serializer.data})
        else:
            query = BlogPost.objects.all()
            results = self.paginate_queryset(query, request, view=self)
            serializer = BlogPostSerializer(results,many=True)
            return self.get_paginated_response({"data":serializer.data})

    def post(self, request, *args, **kwargs):
        query = request.data
        serializer = BlogPostSerializer(data=query)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self,request,pk):
        saved_blogpost = get_object_or_404(BlogPost.objects.all(), pk=pk)
        data = request.data
        serializer = BlogPostSerializer(instance=saved_blogpost, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        saved_blogpost = get_object_or_404(BlogPost.objects.all(), pk=pk)
        saved_blogpost.delete()
        return Response({"status": True})



