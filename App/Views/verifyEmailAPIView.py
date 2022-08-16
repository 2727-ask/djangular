from unicodedata import name
import jwt
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status


from App.models import Profile
from ..serializers import SignUpUserSerializer


class VerifyEmailAPIView(APIView):
    def post(self, request):
        token = request.data.get("token")
        if(token):
            user_details = jwt.decode(token, "secret", algorithms=["HS256"])
            print(user_details)
            serializer = SignUpUserSerializer(data={"username": user_details.get(
                "email"), "password": user_details.get("password")})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                profile = Profile(user=User.objects.get(username=user_details.get("email")), is_verified=True, name=user_details.get("username"))
                profile.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"msg": "Invalid Data, Verification token not found"}, exception=True, status=400)
