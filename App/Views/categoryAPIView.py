from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Category
from ..serializers import CategorySerializer

# Create your views here.

class CategoryAPIView(APIView):
    serializer_class = CategorySerializer
    def get(self,request,pk=None):
        if(pk):
            query = Category.objects.filter(id=pk)
            serializer = CategorySerializer(query,many=True)
            return Response({"data": serializer.data})
        else:
            query = Category.objects.all()
            serializer = CategorySerializer(query,many=True)
            return Response({"data":serializer.data})

    def post(self, request, *args, **kwargs):
        query = request.data
        serializer = CategorySerializer(data=query)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self,request,pk):
        saved_category = get_object_or_404(Category.objects.all(), pk=pk)
        data = request.data
        serializer = CategorySerializer(instance=saved_category, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        saved_category = get_object_or_404(Category.objects.all(), pk=pk)
        saved_category.delete()
        return Response({"status": True})



