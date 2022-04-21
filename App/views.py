from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer

# Create your views here.

class CategoryAPIView(APIView):
    def get(self,request,pk=None):
        if(pk):
            query = Category.objects.filter(id=pk)
            serializer = CategorySerializer(query,many=True)
            return Response({"data": serializer.data})
        else:
            query = Category.objects.all()
            serializer = CategorySerializer(query,many=True)
            return Response({"data":serializer.data})

    def post(self, request):
        query = request.data.get('category')
        serializer = CategorySerializer(data=query)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({"status":True})

    def put(self,request,pk):
        saved_category = get_object_or_404(Category.objects.all(), pk=pk)
        data = request.data.get('category')
        serializer = CategorySerializer(instance=saved_category, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({"status": True})

    def delete(self, request, pk):
        saved_category = get_object_or_404(Category.objects.all(), pk=pk)
        saved_category.delete()
        return Response({"status": True})


class WelcomeAPI(APIView):
    def get(self, request):
        return Response({"msg":"Welcome To Djangular Jenkin Rocks  Hello World!! Hello Yash Yash Changed Something 123"})

