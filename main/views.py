from .serializers import SnippetSerializer
from .models import Snippet
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings


class Views:
    @api_view(["POST"])
    def SendMail(request):
        if request.method == "POST":
            try:
                mail = request.data.get("mail")
                sub = request.data.get("sub")
                msg = request.data.get("msg")
                recipients = request.data.get("recipients")
                passWord = request.data.get("pass")
                if not passWord:
                    return Response("Password Required!")
                send_mail(
                    subject=sub,
                    message=msg,
                    from_email=mail,
                    recipient_list=recipients,
                    auth_user=mail,
                    auth_password=passWord,
                    fail_silently=False,
                )
                return Response("Email sent to all the recipients", status=status.HTTP_200_OK)
            except ValueError:
                print(ValueError)
