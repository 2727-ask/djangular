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
        query = request.GET.get('q', None)
        profile = Profile.objects.filter(user=query)
        if(profile):
            serializer = ProfileSerializer(profile, many=True)
            return Response({"data": serializer.data})
        return Response({"msg": "Profile Not Found"}, exception=True, status=400)

    def post(self, request):
        query = request.data
        profile = Profile.objects.filter(user=request.user)
        if(profile):
            return Response({"msg": "Profile is Already Created"}, exception=True, status=400)
        serializer = ProfileSerializer(data=query)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"data": serializer.data})

    def patch(self, request):
        query = request.data
        profile = Profile.objects.get(user=request.user)
        profile.name = query.get('name', profile.name)
        profile.bio = query.get('bio', profile.bio)
        profile.github = query.get('github', profile.github)
        profile.social = query.get('social', profile.social)
        profile.location = query.get('location', profile.location)
        profile.save()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

