from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from ..models import PasswordResetOTP
from random import randint


class ForgotPasswordAPIView(APIView):

    def random_with_N_digits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

    def post(self, request):
        user = User.objects.filter(username=request.data.get("email"))
        if(user):
            userInfo = User.objects.get(username=request.data.get("email"))
            otp = self.random_with_N_digits(7)
            PasswordResetOTP.objects.update_or_create(user=userInfo, defaults={"otp":otp})
            send_mail('Change Password LinkCode',
                      "Email to reset your password",
                      'ashutoshkumbhar27@gmail.com',
                      [request.data.get("email")],
                      html_message=f'<!doctype html> <html lang="en-US"> <head> <meta content="text/html; charset=utf-8" http-equiv="Content-Type" /> <title>Reset Password Email Template</title> <meta name="description" content="Reset Password Email Template."> <style type="text/css"> a:hover </style> </head> <body marginheight="0" topmargin="0" marginwidth="0" style="margin: 0px; background-color: #f2f3f8;" leftmargin="0">  <table cellspacing="0" border="0" cellpadding="0" width="100%" bgcolor="#f2f3f8" style="@import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,400,600,700); font-family: "Open Sans", sans-serif;"> <tr> <td> <table style="background-color: #f2f3f8; max-width:670px; margin:0 auto;" width="100%" border="0" align="center" cellpadding="0" cellspacing="0"> <tr> <td style="height:80px;"> </td> </tr> <tr> <td style="text-align:center;"> <a href="https://linkcode.in" title="logo" target="_blank"> <img width="160" src="https://linkcode-assets.s3.ap-south-1.amazonaws.com/WhatsApp+Image+2022-08-10+at+10.00.35+PM.jpeg" title="logo" alt="logo"> </a> </td> </tr> <tr> <td style="height:20px;"> </td> </tr> <tr> <td> <table width="95%" border="0" align="center" cellpadding="0" cellspacing="0" style="max-width:670px;background:#fff; border-radius:3px; text-align:center;-webkit-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);-moz-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);box-shadow:0 6px 18px 0 rgba(0,0,0,.06);"> <tr> <td style="height:40px;"> </td> </tr> <tr> <td style="padding:0 35px;"> <h1 style="color:#1e1e2d; font-weight:500; margin:0;font-size:32px;font-family:"Rubik",sans-serif;">You have requested to reset your password</h1> <span style="display:inline-block; vertical-align:middle; margin:29px 0 26px; border-bottom:1px solid #cecece; width:100px;"></span> <p style="color:#455056; font-size:15px;line-height:24px; margin:0;"> We cannot simply send you your old password. A unique link to reset your password has been generated for you. To reset your password, click the following link and follow the instructions. </p> <a href="{settings.SITE_DOMAIN}/auth/forgot-password/change/?token={otp}" style="background:rgb(112.520718, 44.062154, 249.437846);text-decoration:none !important; font-weight:500; margin-top:35px; color:#fff;text-transform:uppercase; font-size:14px;padding:10px 24px;display:inline-block;border-radius:50px;">Reset Password</a> </td> </tr> <tr> <td style="height:40px;"> </td> </tr> </table> </td> <tr> <td style="height:20px;"> </td> </tr> <tr> <td style="text-align:center;"> <p style="font-size:14px; color:rgba(69, 80, 86, 0.7411764705882353); line-height:18px; margin:0 0 0;">© <strong>www.linkcode.in</strong></p> </td> </tr> <tr> <td style="height:80px;"> </td> </tr> </table> </td> </tr> </table>  </body> </html>'
                      )
            return Response(data={"msg": "Password reset email is sent"}, exception=False, status=201)
        else:
            return Response(data={"msg": "Email Not Found"}, exception=True, status=400)
