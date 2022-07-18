from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from ..serializers import SignUpUserSerializer


class SignUpAPIView(APIView):
    def get(self, request):
        print(request.data)
        return Response({"data": "Hello"})

    def post(self, request):
        print(request.data)
        user = User.objects.filter(username=request.data.get("username"))
        if(user):
            return Response({"msg":"This Email is Already Registered"},exception=True,status=400)
        else:
            serializer = SignUpUserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    




