from ..models import Profile
from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from ..serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


import re


def solve(s):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat, s):
        return True
    return False


class ProfileAPIView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        print(request.data)
        return Response({"data": "Hello"})

    def post(self, request):
        query = request.data
        profile = Profile.objects.filter(user=request.user)
        if(profile):
            return Response({"msg":"Profile is Already Created"},exception=True,status=400)
        serializer = ProfileSerializer(data=query)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"data": serializer.data})

    def patch(self, request):
        query = request.data
        profile = Profile.objects.get(user=request.user)
        print(profile)
        print(query)
        print(request.user)
        profile.name = query.get('name',profile.name)
        profile.bio = query.get('bio',profile.bio)
        profile.github = query.get('github',profile.github)
        profile.social = query.get('social',profile.social)
        profile.location = query.get('location',profile.location)
        serializer = ProfileSerializer(profile)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
