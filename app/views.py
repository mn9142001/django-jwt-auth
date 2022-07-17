from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomToken
from rest_framework.views import APIView
from rest_framework.response import Response
class CustomView(TokenObtainPairView):
    serializer_class = CustomToken


class NewView(APIView):
    def post(self, request):
        return Response({'hello': request.user.username})
