import jwt
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail



from App.models import Profile
from ..serializers import SignUpUserSerializer


import re


def solve(s):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat, s):
        return True
    return False


def sanitizeRequest(request):
    if(request.data.get("username") == None or request.data.get("password") == None or request.data.get("email") == None):
        return {"msg": "Incomplete Data Provided", "status": False}
    if(len(request.data.get("password")) < 7):
        return {"msg": "Password must be atleast 8 charachters long", "status": False}
    return {"msg": "The request is correct", "status": True}


class SignUpAPIView(APIView):
    def get(self, request):
        print(request.data)
        return Response({"data": "Hello"})

    def post(self, request):
        if(sanitizeRequest(request).get("status") == True):
            user = User.objects.filter(username=request.data.get("email"))
            if(user):
                return Response({"msg": "This Email is Already Registered"}, exception=True, status=400)
            else:
                if(solve(request.data.get("email"))):
                    # print(request.data)
                    encoded_jwt = jwt.encode(request.data, "secret", algorithm="HS256").decode("utf-8") 
                    send_mail(
                        'Verification Email For LinkCode Account',
                        f'Please click on below link to verify your account: {settings.SITE_DOMAIN}/auth/verifying/?token={encoded_jwt}',
                        'ashutoshkumbhar27@gmail.com',
                        [request.data.get("email")],
                        html_message=f"<h2>Welcome To LinkCode Technologies</h2><hr></br><img style='width:200px; display:grid; place-items:center' src='https://linkcode-assets.s3.ap-south-1.amazonaws.com/WhatsApp+Image+2022-08-10+at+10.00.35+PM.jpeg'></br><h5>Please verify your account by clicking on the button</h5><br><a href='{settings.SITE_DOMAIN}/auth/verifying/?token={encoded_jwt}'>Click Here To Verify</a>"
                    )
        else:
            return Response({"msg": sanitizeRequest(request).get("msg")}, exception=True, status=400)

        return Response({"data": "Hello"})

    # def post(self, request):
    #     if(sanitizeRequest(request).get("status") == True):
    #         user = User.objects.filter(username=request.data.get("username"))
    #         if(user):
    #             return Response({"msg":"This Email is Already Registered"},exception=True,status=400)
    #         else:
    #             if(solve(request.data.get("username"))):
    #                 serializer = SignUpUserSerializer(data=request.data)
    #                 if serializer.is_valid(raise_exception=True):
    #                     serializer.save()
    #                     profile = Profile(user=User.objects.get(username=request.data.get("username")))
    #                     profile.save()
    #                 return Response(serializer.data, status=status.HTTP_201_CREATED)
    #             return Response({"msg":"Enter Valid Email Address"},exception=True,status=400)
    #     else:
    #         return Response({"msg":sanitizeRequest(request).get("msg")},exception=True,status=400)
