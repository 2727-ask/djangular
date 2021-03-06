from datetime import datetime
from pickle import FALSE
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from App.models import Profile
from ..serializers import SignUpUserSerializer


import re

def solve(s):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   return False


def sanitizeRequest(request):
    if(request.data.get("username")==None or request.data.get("password")==None):
        return {"msg":"Incomplete Data Provided", "status":False}
    if(len(request.data.get("password"))<=5):
        return {"msg":"Password is too short", "status":False}
    return {"msg":"The request is correct", "status":True}     



class SignUpAPIView(APIView):
    def get(self, request):
        print(request.data)
        return Response({"data": "Hello"})

    def post(self, request):
        if(sanitizeRequest(request).get("status") == True):
            user = User.objects.filter(username=request.data.get("username"))
            if(user):
                return Response({"msg":"This Email is Already Registered"},exception=True,status=400)
            else:
                if(solve(request.data.get("username"))):
                    serializer = SignUpUserSerializer(data=request.data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
                        profile = Profile(user=User.objects.get(username=request.data.get("username")))
                        profile.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED) 
                return Response({"msg":"Enter Valid Email Address"},exception=True,status=400)     
        else:
            return Response({"msg":sanitizeRequest(request).get("msg")},exception=True,status=400)   


